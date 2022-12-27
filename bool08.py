from math import *


def main(a):
    """
    check the whole number. Integers are 0 and a positive number.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    x = floor(a)
    return x == a >= 0


print(main(-1))
