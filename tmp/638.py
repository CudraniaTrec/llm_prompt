import math

def wind_chill(velocity, temperature):
    index = 13.12 + 0.6215 * temperature - 11.37 * (velocity ** 0.16) + 0.3965 * temperature * (velocity ** 0.16)
    return math.ceil(index)
assert wind_chill(120,35)==40
assert wind_chill(40,20)==19
assert wind_chill(10,8)==6