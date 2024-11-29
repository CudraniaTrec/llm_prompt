import cmath
import math

def polar_rect(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    rectangular_coordinates = (x, y)
    complex_form = complex(x, y)
    return rectangular_coordinates, complex_form
import cmath
import math

def polar_rect(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    rectangular_coordinates = (x, y)
    complex_form = complex(x, y)
    return rectangular_coordinates, complex_form

assert polar_rect(3, 4) == ((-1.1892071200000001, -2.774647912440031), (-1.1892071200000001-2.774647912440031j))
import cmath
import math

def polar_rect(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    rectangular_coordinates = (x, y)
    complex_form = complex(x, y)
    return rectangular_coordinates, complex_form

assert polar_rect(3, 4) == ((-1.1892071200000001, -2.774647912440031), (-1.1892071200000001-2.774647912440031j))
assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
assert polar_rect(4,7)==((8.06225774829855, 1.0516502125483738), (-2+2.4492935982947064e-16j))
assert polar_rect(15,17)==((22.67156809750927, 0.8478169733934057), (-2+2.4492935982947064e-16j))