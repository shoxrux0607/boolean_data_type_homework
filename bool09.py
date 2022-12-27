from math import *


def main(a):
    """
    Check the natural number. Natural numbers are numbers used in counting.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here

    x = floor(a)
    return x == a > 0


print(main(-2))
