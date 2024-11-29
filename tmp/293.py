import math

def otherside_rightangle(side1, side2):
    return math.sqrt(side1**2 + side2**2)
assert otherside_rightangle(7,8)==10.63014581273465
assert otherside_rightangle(3,4)==5
assert otherside_rightangle(7,15)==16.55294535724685