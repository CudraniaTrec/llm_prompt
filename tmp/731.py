import math

def lateralsurface_cone(r, h):
    slant_height = math.sqrt(r**2 + h**2)
    lateral_surface_area = math.pi * r * slant_height
    return lateral_surface_area
import math

def lateralsurface_cone(r, h):
    slant_height = math.sqrt(r**2 + h**2)
    lateral_surface_area = math.pi * r * slant_height
    return lateral_surface_area

assert lateralsurface_cone(5,12) == 204.20352248333654
assert lateralsurface_cone(5,12)==204.20352248333654
assert lateralsurface_cone(10,15)==566.3586699569488
assert lateralsurface_cone(19,17)==1521.8090132193388