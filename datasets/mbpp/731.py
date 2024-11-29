#Write a function to find the lateral surface area of a cone given radius r and the height h.
import math
def lateralsurface_cone(r,h):
  l = math.sqrt(r * r + h * h)
  LSA = math.pi * r  * l
  return LSA