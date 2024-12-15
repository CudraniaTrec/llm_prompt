import json

mbpp = json.load(open("sanitized-mbpp.json"))
max_codelen_mbpp = max([len(d['code']) for d in mbpp])
max_codelines_mbpp = max([d['code'].count('\n') + 1 for d in mbpp])
avg_codelen_mbpp = sum([len(d['code']) for d in mbpp]) / len(mbpp)
avg_codelines_mbpp = sum([d['code'].count('\n') + 1 for d in mbpp]) / len(mbpp)

humaneval = json.load(open("HumanEval.json"))
max_codelen_humaneval = max([len(d['canonical_solution']) for d in humaneval])
max_codelines_humaneval = max([d['canonical_solution'].count('\n') + 1 for d in humaneval])
avg_codelen_humaneval = sum([len(d['canonical_solution']) for d in humaneval]) / len(humaneval)
avg_codelines_humaneval = sum([d['canonical_solution'].count('\n') + 1 for d in humaneval]) / len(humaneval)

mathqa = json.load(open("mathqa-python-test.json"))
max_codelen_mathqa = max([len(d['code']) for d in mathqa])
max_codelines_mathqa = max([d['code'].count('\n') + 1 for d in mathqa])
avg_codelen_mathqa = sum([len(d['code']) for d in mathqa]) / len(mathqa)
avg_codelines_mathqa = sum([d['code'].count('\n') + 1 for d in mathqa]) / len(mathqa)

print(max_codelen_mbpp, max_codelen_mathqa, max_codelen_humaneval)
print(max_codelines_mbpp, max_codelines_mathqa, max_codelines_humaneval)
print(avg_codelen_mbpp, avg_codelen_mathqa, avg_codelen_humaneval)
print(avg_codelines_mbpp, avg_codelines_mathqa, avg_codelines_humaneval)