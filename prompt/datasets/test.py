import json
from contain_rec import has_recursive_call

rec_cnt=0

mbpp = json.load(open("sanitized-mbpp.json"))
max_codelen_mbpp = max([len(d['code']) for d in mbpp])
max_codelines_mbpp = max([d['code'].count('\n') + 1 for d in mbpp])
avg_codelen_mbpp = sum([len(d['code']) for d in mbpp]) / len(mbpp)
avg_codelines_mbpp = sum([d['code'].count('\n') + 1 for d in mbpp]) / len(mbpp)
for d in json.load(open('mbpp.json')):
    if has_recursive_call(d['code']):
        rec_cnt+=1
        print(f"mbpp: {d['task_id']}")
        # print(d['code'])

humaneval = json.load(open("HumanEval.json"))
max_codelen_humaneval = max([len(d['canonical_solution']) for d in humaneval])
max_codelines_humaneval = max([d['canonical_solution'].count('\n') + 1 for d in humaneval])
avg_codelen_humaneval = sum([len(d['canonical_solution']) for d in humaneval]) / len(humaneval)
avg_codelines_humaneval = sum([d['canonical_solution'].count('\n') + 1 for d in humaneval]) / len(humaneval)
for d in humaneval:
    code = d['prompt']+d['canonical_solution']
    if has_recursive_call(code):
        rec_cnt+=1
        print(f"humaneval: {d['task_id']}")
        print(code)

mathqa = json.load(open("mathqa-python-test.json"))
max_codelen_mathqa = max([len(d['code']) for d in mathqa])
max_codelines_mathqa = max([d['code'].count('\n') + 1 for d in mathqa])
avg_codelen_mathqa = sum([len(d['code']) for d in mathqa]) / len(mathqa)
avg_codelines_mathqa = sum([d['code'].count('\n') + 1 for d in mathqa]) / len(mathqa)
for d in mathqa:
    if has_recursive_call(d['code']):
        rec_cnt+=1
        print(f"mathqa: {d['task_id']}")
        print(d['code'])

print(max_codelen_mbpp, max_codelen_mathqa, max_codelen_humaneval)
print(max_codelines_mbpp, max_codelines_mathqa, max_codelines_humaneval)
print(avg_codelen_mbpp, avg_codelen_mathqa, avg_codelen_humaneval)
print(avg_codelines_mbpp, avg_codelines_mathqa, avg_codelines_humaneval)

print(f"rec_cnt: {rec_cnt}")

mathqa_test = json.load(open("mathqa-python-test.json"))
for d in mathqa_test:
    if "text" in d:
        d["prompt"] = d["text"]
        del d["text"]
json.dump(mathqa_test, open("mathqa-python-test.json", "w"), indent=2)
mathqa_challenge = json.load(open("mathqa-python-challenge.json"))
for d in mathqa_challenge:
    if "text" in d:
        d["prompt"] = d["text"]
        del d["text"]
json.dump(mathqa_challenge, open("mathqa-python-challenge.json", "w"), indent=2)
mathqa_train = json.load(open("mathqa-python-train.json"))
for d in mathqa_train:
    if "text" in d:
        d["prompt"] = d["text"]
        del d["text"]
json.dump(mathqa_train, open("mathqa-python-train.json", "w"), indent=2)