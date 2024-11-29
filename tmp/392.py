def get_max_sum(n):
    if n == 0:
        return 0
    return max(get_max_sum(n // 2) + get_max_sum(n // 3) + get_max_sum(n // 4) + get_max_sum(n // 5), n)
assert get_max_sum(60) == 106
assert get_max_sum(10) == 12
assert get_max_sum(2) == 2