import math

def polysum(n, s):
    """
    takes in n = number of sides, s = side length
    returns sum of area + perimeter^2 to 4 dp.
    """
    area = (0.25*n*s**2) / (math.tan(math.pi/n))
    peri = n*s
    return round(area + peri**2, 4)
