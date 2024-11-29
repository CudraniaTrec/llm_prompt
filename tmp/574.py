import math

def surfacearea_cylinder(height, radius):
    lateral_surface_area = 2 * math.pi * radius * height
    top_bottom_area = 2 * math.pi * radius ** 2
    total_surface_area = lateral_surface_area + top_bottom_area
    return round(total_surface_area, 2)
import math

def surfacearea_cylinder(height, radius):
    lateral_surface_area = 2 * math.pi * radius * height
    top_bottom_area = 2 * math.pi * radius ** 2
    total_surface_area = lateral_surface_area + top_bottom_area
    return round(total_surface_area, 2)

assert surfacearea_cylinder(10, 5) == 942.45
import math

def surfacearea_cylinder(height, radius):
    lateral_surface_area = 2 * math.pi * radius * height
    top_bottom_area = 2 * math.pi * radius ** 2
    total_surface_area = lateral_surface_area + top_bottom_area
    return round(total_surface_area, 2)

assert surfacearea_cylinder(10, 5) == 942.48
assert surfacearea_cylinder(10,5)==942.45
assert surfacearea_cylinder(4,5)==226.18800000000002
assert surfacearea_cylinder(4,10)==351.848