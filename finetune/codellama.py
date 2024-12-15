import torch, os
import random, numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoConfig
from utils import codegen_direct, set_seed

os.environ["CUDA_VISIBLE_DEVICES"] = "0,2,3"
os.environ["TOKENIZERS_PARALLELISM"] = "true"
checkpoint = "codellama/CodeLlama-7b-Python-hf"
set_seed(321876902)

def test_codellama():
    tokenizer = AutoTokenizer.from_pretrained(checkpoint, use_fast=True, local_files_only=True)
    # for fp16 use `torch_dtype=torch.float16` instead
    model = AutoModelForCausalLM.from_pretrained(checkpoint, 
                                                device_map="auto",
                                                local_files_only=True, 
                                                torch_dtype=torch.bfloat16)
    config = AutoConfig.from_pretrained(checkpoint, local_files_only=True)
    print(config)
    print(model)
    print("="*20+"test codellama"+"="*20)
    input_string = """
    # Complete the following task in Python. 
    # Write a function to find the n largest integers from a given list of numbers, returned in descending order.
    # Please respond with code only, no explanation, no example IO, no annotations.
    # Your code should be able to pass the following test cases.
    # assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
    # assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[85, 75, 65, 58, 35]
    def
    """
    inputs = tokenizer.encode(input_string, return_tensors="pt").to("cuda")
    outputs = model.generate(inputs, 
                            pad_token_id=tokenizer.eos_token_id,
                            attention_mask=torch.ones_like(inputs), 
                            max_length=500)
    print(tokenizer.decode(outputs[0]))
    print(f"Memory footprint: {model.get_memory_footprint() / 1e6:.2f} MB")

# generate input to the model and process the output
def get_input(problem,dataset,tokenizer):
    if dataset == "mbpp":
        question = "Complete the following task in Python.\n"
        question += problem['prompt']
        question += "\nPlease respond with code only, no explanations, no example IOs, no annotations and no print statements.\n"
        question += "\nYour code should be able to solve the following test cases:\n"
        question += "\n".join(problem['test_list'])
        # add # to the beginning of each line
        question = "\n".join(["# "+line for line in question.splitlines()])
        question += "\ndef"
    elif dataset == "humaneval":
        question = "# Complete the following python code, according to the docstring:\n"
        question += "\n# Please respond with code only, no explanations, no example IOs, no annotations and no print statements.\n"
        question += problem['prompt']
    elif dataset == "mathqa":
        question = "# Write a python program to solve the following math problem:\n"
        question += f"{problem['text']}"
        question += "\n# You don't have to define any functions or methods, just name the final result variable as `answer`:\n"
        question += "```python\n"
    else:
        raise ValueError("Invalid dataset: "+dataset)
    return question
def process_output(code,tokenizer):
    lines = code.splitlines()
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
    # test_codellama()
    codegen_direct(model="codellama-python",
    dataset="mathqa",
    get_input=get_input,
    process_output=process_output)
