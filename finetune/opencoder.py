import torch,os
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoConfig
from utils import set_seed,codegen_direct

set_seed(321876902)
os.environ["TOKENIZERS_PARALLELISM"] = "true"
os.environ["CUDA_VISIBLE_DEVICES"] = "2,3"
model_name = "infly/OpenCoder-1.5B-Instruct"

def test_opencoder():
    model = AutoModelForCausalLM.from_pretrained(model_name,
                                                 torch_dtype=torch.bfloat16,
                                                 device_map="auto",
                                                 trust_remote_code=True,
                                                 local_files_only=True)
    tokenizer = AutoTokenizer.from_pretrained(model_name,
                                              use_fast=True,
                                              trust_remote_code=True,
                                              local_files_only=True)
    config = AutoConfig.from_pretrained(model_name, local_files_only=True)
    print(config)
    print(model)
    # 打印特殊 token 及其 ID
    print("Special Tokens and their IDs:")
    for token_name, token in tokenizer.special_tokens_map.items():
        token_id = tokenizer.convert_tokens_to_ids(token)
        print(f"{token_name}: '{token}' (ID: {token_id})")
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
    messages0=[
        { 'role': 'user', 'content': question2 }
    ]
    text0 = tokenizer.apply_chat_template(
        messages0,
        tokenize=False,
        add_generation_prompt=True,
    )
    messages1 = [
        { 'role': 'user', 'content': question1 }
    ]
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
    print(inputs)
    outputs = model.generate(**inputs,
                             pad_token_id=tokenizer.pad_token_id,
                             max_new_tokens=1024,
                             do_sample=False)
    print(outputs)
    result = tokenizer.decode(outputs[1], skip_special_tokens=True)
    print(process_output(result,tokenizer))

def get_input(problem,dataset,tokenizer):
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
        question += problem['text']
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

def process_output(output,tokenizer):
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

if __name__ == "__main__":
    # test_opencoder()
    codegen_direct("qwen7","mathqa",get_input,process_output)