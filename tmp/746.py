import math

def sector_area(radius, angle):
    if angle > 360:
        return None
    return (angle / 360) * math.pi * (radius ** 2)
assert sector_area(4,45)==6.283185307179586
assert sector_area(9,45)==31.808625617596654
assert sector_area(9,361)==None