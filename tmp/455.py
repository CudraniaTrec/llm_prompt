def check_monthnumb_number(month):
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12.")
    return month in [1, 3, 5, 7, 8, 10, 12]
assert check_monthnumb_number(5)==True
assert check_monthnumb_number(2)==False
assert check_monthnumb_number(6)==False