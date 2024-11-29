def is_decimal(s):
    try:
        parts = s.split('.')
        if len(parts) == 2 and len(parts[1]) == 2:
            float(s)
            return True
        return False
    except ValueError:
        return False
        if len(parts) == 2 and len(parts[1]) == 2:
            float(s)
        if len(parts) != 2:
            return False
        if len(parts[1]) != 2:
            return False
        float(s)
        return True
assert is_decimal('123.11')==True
assert is_decimal('e666.86')==False
assert is_decimal('3.124587')==False
assert is_decimal('1.11')==True
assert is_decimal('1.1.11')==False