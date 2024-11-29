def rearrange_bigger(num):
    digits = list(str(num))
    n = len(digits)

    # Step 1: Find the first decreasing element from the right
    i = n - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    if i == -1:
        return -1  # No bigger number possible

    # Step 2: Find the smallest element on right of the found element
    j = n - 1
    while digits[j] <= digits[i]:
        j -= 1

    # Step 3: Swap the two elements
    digits[i], digits[j] = digits[j], digits[i]

    # Step 4: Reverse the elements to the right of i
    digits = digits[:i + 1] + sorted(digits[i + 1:])

    return int(''.join(digits))
assert rearrange_bigger(12)==21
assert rearrange_bigger(10)==False
assert rearrange_bigger(102)==120