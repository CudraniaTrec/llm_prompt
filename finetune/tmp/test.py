import json
json.load(open('mbpp_test.json'))

from datasets import load_dataset
dataset = load_dataset('json', data_files='mbpp_test.json')
print(dataset)