from datasets import load_dataset
datas_test= load_dataset("dtruong46me/mathqa-python", split="test")

datas = []
import beeprint as bp
for data in datas_test:
    datas.append({
        'prompt': data['text'],
        'code': data['code'],
        'rationale': data['reasoning'],
        'answer': data['answer'],
        'task_id': data['task_id'],
    })
    if len(datas) == 1:
        bp.pp(datas)
#dump to json
import json
with open('mathqa-python-test.json', 'w') as f:
    json.dump(datas, f)