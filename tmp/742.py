import math

def area_tetrahedron(side_length):
    return math.sqrt(2) * side_length**2
assert area_tetrahedron(3)==15.588457268119894
assert area_tetrahedron(20)==692.8203230275509
assert area_tetrahedron(10)==173.20508075688772