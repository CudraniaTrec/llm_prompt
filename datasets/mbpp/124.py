#Write a function to get the angle of a complex number.
import cmath
def angle_complex(a,b):
  cn=complex(a,b)
  angle=cmath.phase(a+b)
  return angle