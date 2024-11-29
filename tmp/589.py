def perfect_squares(start, end):
    return [i**2 for i in range(int(start**0.5), int(end**0.5) + 1) if i**2 >= start and i**2 <= end]
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
assert perfect_squares(50,100)==[64, 81, 100]
assert perfect_squares(100,200)==[100, 121, 144, 169, 196]