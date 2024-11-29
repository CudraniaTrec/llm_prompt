def len_log(words):
    longest_length = 0
    for word in words:
        longest_length = max(longest_length, len(word))
    return longest_length
assert len_log(["python","PHP","bigdata"]) == 7
assert len_log(["a","ab","abc"]) == 3
assert len_log(["small","big","tall"]) == 5