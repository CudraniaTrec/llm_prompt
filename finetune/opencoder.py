import torch,os
from torch.utils.data import DataLoader
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoConfig, TrainingArguments, Trainer
from utils import set_seed, codegen_direct, config, prepare_data, print_special_tokens
from utils import EarlyStoppingCallback, find_checkpoint_path, find_checkpoint

set_seed(config['seed'])
os.environ["TOKENIZERS_PARALLELISM"] = "true"
# os.environ["CUDA_VISIBLE_DEVICES"] = "4"

# example inference
def test_opencoder(model=None):
    if not model:
        model = 'qwen1.5'
    checkpoint, _, _ = find_checkpoint_path(model)
    model = AutoModelForCausalLM.from_pretrained(checkpoint,
                                                 torch_dtype=torch.bfloat16,
                                                 device_map="auto",
                                                 trust_remote_code=True,
                                                 local_files_only=True)
    tokenizer = AutoTokenizer.from_pretrained(checkpoint,
                                              use_fast=True,
                                              trust_remote_code=True,
                                              local_files_only=True)
    question1 = """Write a python program to solve the following math problem:
what will be the difference between simple and compound interest at 14 % per annum on a sum of rs . 1000 after 4 years ? 
n0 = 14.0 n1 = 1000.0 n2 = 4.0
You don't have to define any functions or methods, just name the final result variable as `answer`:"""
    question2 = """Complete the following task in Python. 
Write a function to find the n largest integers from a given list of numbers, returned in descending order.
Please respond with code only, no explanation, no example IO, no annotations.
Your code should be able to pass the following test cases.
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[85, 75, 65, 58, 35]"""
    messages0=[{ 'role': 'user', 'content': question2 }]
    text0 = tokenizer.apply_chat_template(
        messages0,
        tokenize=False,
        add_generation_prompt=True,
    )
    messages1 = [ { 'role': 'user', 'content': question1 }]
    text1 = tokenizer.apply_chat_template(
        messages1,
        tokenize=False,
        add_generation_prompt=True,
    )
    inputs = tokenizer([text0,text1],
                       padding=True,
                       padding_side="left",
                       truncation=True,
                       max_length=1024,
                       return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs,
                             pad_token_id=tokenizer.pad_token_id,
                             max_new_tokens=1024,
                             do_sample=False)
    result = tokenizer.decode(outputs[1], skip_special_tokens=True)
    print(process_output(result,tokenizer))

# generate prompt to the opencoder/qwen
def get_input(problem, dataset, tokenizer):
    if dataset == "mbpp":
        question = "Complete the following task in Python.\n"
        question += problem['prompt']
        question += "\nPlease respond with code only, no explanations, no example IOs, no annotations and no print statements.\n"
        question += "\nYour code should be able to solve the following test cases:\n"
        question += "\n".join(problem['test_list'])
    elif dataset == "humaneval":
        question = "Complete the following python code, according to the docstring:\n"
        question += "Please respond with code only, no explanations, no example IOs, no annotations and no print statements.\n"
        question += "```python\n"
        question += problem['prompt']
        question += "\n```\n"
    elif dataset == "mathqa":
        question = "Write a python program to solve the following math problem:\n"
        question += problem['prompt']
        question += "\nYou don't have to define any functions or methods, just name the final result variable as `answer`:\n"
    else:
        raise ValueError(f"dataset {dataset} not supported")
    messages = [
        {'role': 'user', 'content': question}
    ]
    return tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

# extract code from the opencoder/qwen output
def process_output(output, tokenizer):
    # remove the chat history
    lines = output.splitlines()
    assistant_lineno = lines.index("assistant")
    lines=lines[assistant_lineno+1:]
    # retrieve the code block
    if "```python" in lines:
        start_lineno = lines.index("```python")+1
        try:
            end_lineno = lines.index("```",start_lineno)
        except:
            end_lineno = len(lines)
        lines=lines[start_lineno:end_lineno]
    # remove replicated \n and annotations
    code = "\n".join([line for line in lines
                      if line.strip() and not line.strip().startswith("#")])
    return code.replace(tokenizer.eos_token,"").replace(tokenizer.pad_token,"")

# finetune the model
def finetune(model_name, dataset_name):
    model_name = find_checkpoint(model_name)
    dataset = prepare_data(dataset_name)
    model = AutoModelForCausalLM.from_pretrained(model_name,
                                                 torch_dtype=torch.bfloat16,
                                                 device_map="auto",
                                                 trust_remote_code=True,
                                                 local_files_only=True)
    tokenizer = AutoTokenizer.from_pretrained(model_name,
                                              use_fast=True,
                                              trust_remote_code=True,
                                              local_files_only=True)
    def preprocess_function(examples):
        new_examples = []
        for i in range(len(examples['prompt'])):
            problem = {key: examples[key][i] for key in examples.keys()}
            new_examples.append(problem)
        inputs = [get_input(example, dataset_name, tokenizer) for example in new_examples]
        outputs = [code + tokenizer.eos_token for code in examples['code']]
        tokenized_inputs = tokenizer(inputs,
                                     padding=True,
                                     padding_side='left',
                                     truncation=True,
                                     max_length=config['max_input_length'])
        tokenized_outputs = tokenizer(outputs,
                                      padding=True,
                                      truncation=True,
                                      max_length=config['max_output_length'])
        model_inputs = tokenized_inputs
        model_inputs["labels"] = [
            [-100] * len(input_ids) + output_ids
            for input_ids, output_ids in zip(tokenized_inputs["input_ids"], tokenized_outputs["input_ids"])
        ]
        model_inputs["input_ids"] = [
            input_ids + output_ids
            for input_ids, output_ids in zip(tokenized_inputs["input_ids"], tokenized_outputs["input_ids"])
        ]
        model_inputs["attention_mask"] = [
            input_mask + output_mask
            for input_mask, output_mask in zip(tokenized_inputs["attention_mask"], tokenized_outputs["attention_mask"])
        ]
        return model_inputs
    dataset = dataset.map(preprocess_function, batched=True,
                          batch_size=config['batch_size_train']*torch.cuda.device_count(),
                          remove_columns=dataset['train'].column_names)
    print(dataset)
    def data_collator(datas):
        max_length = max(len(data['input_ids']) for data in datas)
        for data in datas:
            data['input_ids'] += [tokenizer.pad_token_id] * (max_length - len(data['input_ids']))
            data['attention_mask'] += [0] * (max_length - len(data['attention_mask']))
            data['labels'] += [-100] * (max_length - len(data['labels']))
        return {key: torch.tensor([data[key] for data in datas]) for key in datas[0].keys()}
    training_args = TrainingArguments(
        output_dir=f"./output/{model_name}/{dataset_name}",
        overwrite_output_dir=True,
        per_device_train_batch_size=config['batch_size_train'],
        num_train_epochs=5,
        logging_strategy="steps",
        logging_steps=config['log_steps'][dataset_name],
        eval_strategy="steps",
        eval_steps=config['eval_steps'][dataset_name],
        save_strategy="steps",
        save_steps=config['eval_steps'][dataset_name],
        save_total_limit=config['early_stopping_patience']+1,
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        learning_rate=config['learning_rate'][dataset_name],
        seed=config['seed'],
        bf16=True,
        report_to="wandb",
        run_name=f"{model_name}-{dataset_name}",
    )
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["valid"],
        tokenizer=tokenizer,
        data_collator= data_collator,
        callbacks=[EarlyStoppingCallback(config['early_stopping_patience'],1e-5)],
    )
    trainer.train()
    trainer.save_model(f"./output/{model_name}/{dataset_name}/best_model")

if __name__ == "__main__":
    model = 'qwen1.5'
    dataset = 'mathqa'
    model_path= f"output/{find_checkpoint(model)}/{dataset}/best_model"
    codegen_direct(model_path, dataset, get_input, process_output)
    # finetune(model,dataset)