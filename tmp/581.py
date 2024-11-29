def surface_Area(base_edge, height):
    base_area = base_edge ** 2
    slant_height = (height**2 + (base_edge / 2)**2) ** 0.5
    lateral_area = 2 * base_edge * slant_height
    total_surface_area = base_area + lateral_area
    return total_surface_area
assert surface_Area(3,4) == 33
assert surface_Area(4,5) == 56
assert surface_Area(1,2) == 5