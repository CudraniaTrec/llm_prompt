def count_char_position(s):
    count = 0
    s = s.lower()
    for i in range(len(s)):
        if ord(s[i]) - ord('a') == i:
            count += 1
    return count
assert count_char_position("xbcefg") == 2
assert count_char_position("ABcED") == 3
assert count_char_position("AbgdeF") == 5