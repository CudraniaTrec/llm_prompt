def overlapping(seq1, seq2):
    for item in seq1:
        if item in seq2:
            return True
    return False
def overlapping(seq1, seq2):
    for item in seq1:
        if item in seq2:
            return True
    return False
def overlapping(seq1, seq2):
    for item in seq1:
        if item in seq2:
            return True
    return False
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
assert overlapping([1,2,3],[4,5,6]) == False
assert overlapping([1,4,5],[1,4,5]) == True