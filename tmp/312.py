import math
import math

def volume_cone(radius, height):
    return (1/3) * math.pi * (radius ** 2) * height
assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
assert math.isclose(volume_cone(10,15), 1570.7963267948965, rel_tol=0.001)
assert math.isclose(volume_cone(19,17), 6426.651371693521, rel_tol=0.001)