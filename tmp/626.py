def triangle_area(radius):
    if radius <= 0:
        return None
    return (radius ** 2) * (3.14159 / 2)
assert triangle_area(-1) == None
assert triangle_area(0) == 0
assert triangle_area(2) == 4