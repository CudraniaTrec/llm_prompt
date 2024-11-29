#Write a function to calculate the area of a regular polygon given the length and number of its sides.
from math import tan, pi
def area_polygon(s, l):
  area = s * (l ** 2) / (4 * tan(pi / s))
  return area