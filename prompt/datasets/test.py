import json
from contain_rec_loop import has_recursive_call, has_loop_in_code

rec_cnt, loop_cnt = 0, 0
rec_cnt_mbpp, loop_cnt_mbpp = 0, 0
rec_cnt_humaneval, loop_cnt_humaneval = 0, 0
rec_cnt_mathqa, loop_cnt_mathqa = 0, 0

mbpp = json.load(open("sanitized-mbpp.json"))
max_codelen_mbpp = max([len(d['code']) for d in mbpp])
max_codelines_mbpp = max([d['code'].count('\n') + 1 for d in mbpp])
avg_codelen_mbpp = sum([len(d['code']) for d in mbpp]) / len(mbpp)
avg_codelines_mbpp = sum([d['code'].count('\n') + 1 for d in mbpp]) / len(mbpp)
for d in json.load(open('mbpp.json')):
    if has_recursive_call(d['code']):
        rec_cnt+=1
        rec_cnt_mbpp+=1
    if has_loop_in_code(d['code']):
        loop_cnt+=1
        loop_cnt_mbpp+=1

humaneval = json.load(open("HumanEval.json"))
max_codelen_humaneval = max([len(d['canonical_solution']) for d in humaneval])
max_codelines_humaneval = max([d['canonical_solution'].count('\n') + 1 for d in humaneval])
avg_codelen_humaneval = sum([len(d['canonical_solution']) for d in humaneval]) / len(humaneval)
avg_codelines_humaneval = sum([d['canonical_solution'].count('\n') + 1 for d in humaneval]) / len(humaneval)
for d in humaneval:
    code = d['prompt']+d['canonical_solution']
    if has_recursive_call(code):
        rec_cnt+=1
        rec_cnt_humaneval+=1
    if has_loop_in_code(code):
        loop_cnt+=1
        loop_cnt_humaneval+=1

mathqa = json.load(open("mathqa-python-test.json"))
max_codelen_mathqa = max([len(d['code']) for d in mathqa])
max_codelines_mathqa = max([d['code'].count('\n') + 1 for d in mathqa])
avg_codelen_mathqa = sum([len(d['code']) for d in mathqa]) / len(mathqa)
avg_codelines_mathqa = sum([d['code'].count('\n') + 1 for d in mathqa]) / len(mathqa)
for d in mathqa:
    if has_recursive_call(d['code']):
        rec_cnt+=1
        rec_cnt_mathqa+=1
    if has_loop_in_code(d['code']):
        loop_cnt+=1
        loop_cnt_mathqa+=1

print(f"loop_cnt: {loop_cnt}\n  mbpp: {loop_cnt_mbpp}, humaneval: {loop_cnt_humaneval}, mathqa: {loop_cnt_mathqa}")
print(f"rec_cnt: {rec_cnt}\n  mbpp: {rec_cnt_mbpp}, humaneval: {rec_cnt_humaneval}, mathqa: {rec_cnt_mathqa}")
print(f"max code length: mbpp: {max_codelen_mbpp}\n  humaneval: {max_codelen_humaneval}, mathqa: {max_codelen_mathqa}")
print(f"max code lines: mbpp: {max_codelines_mbpp}\n  humaneval: {max_codelines_humaneval}, mathqa: {max_codelines_mathqa}")
print(f"avg code length: mbpp: {avg_codelen_mbpp}\n  humaneval: {avg_codelen_humaneval}, mathqa: {avg_codelen_mathqa}")
print(f"avg code lines: mbpp: {avg_codelines_mbpp}\n  humaneval: {avg_codelines_humaneval}, mathqa: {avg_codelines_mathqa}")