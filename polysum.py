"""
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: 
0.25∗n∗s2
tan(π/n)
 
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. 
This function should sum the area and square of the perimeter of the
regular polygon.

The function returns the sum, rounded to 4 decimal places.
"""


import math

def polysum(n, s):
    """
    takes in n = number of sides, s = side length
    returns sum of area + perimeter^2 to 4 dp.
    """
    area = (0.25*n*s**2) / (math.tan(math.pi/n))
    peri = n*s
    return round(area + peri**2, 4)
