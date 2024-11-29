def min_Swaps(bin1, bin2):
    if len(bin1) != len(bin2):
        return -1
    count = 0
    for b1, b2 in zip(bin1, bin2):
        if b1 != b2:
            count += 1
    return count // 2
assert min_Swaps("1101","1110") == 1
assert min_Swaps("111","000") == "Not Possible"
assert min_Swaps("111","110") == "Not Possible"