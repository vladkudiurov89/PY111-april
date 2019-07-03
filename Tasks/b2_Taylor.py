"""Taylor series"""
from math import factorial


def ex(x) -> float:
    """Calculate value of e^x with Taylor series
	:param x: x value
	:return: e^x value"""
    ox = 1
    n = 1
    for i in range(10):
        ox += (x ** n) / factorial(n)
        n += 1
    return float(ox)


def sinx(x) -> float:
    """Calculate sin(x) with Taylor series
	:param x: x value
	:return: sin(x) value"""

    sin_x = x
    n = 3
    m = 1
    for i in range(10):
        sin_x += -m * (x ** n) / factorial(n)
        m *= -1
        n += 2
    return sin_x
