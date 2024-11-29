import math
import math

def area_polygon(num_sides, side_length):
    if num_sides < 3:
        raise ValueError("A polygon must have at least 3 sides")
    
    # Calculate the area using the formula
    area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
    return area
assert math.isclose(area_polygon(4, 20), 400., rel_tol=0.001)
assert math.isclose(area_polygon(10, 15), 1731.197, rel_tol=0.001)
assert math.isclose(area_polygon(9, 7), 302.909, rel_tol=0.001)