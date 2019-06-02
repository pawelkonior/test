#!/usr/bin/env python3

"""Add two digits

Usage:
    python perferct_module.py Digit1 Digit2
    ./perferct_module.py Digit1 Digit2
    from perfect_module import add
"""
import sys

def add(a, b):
    """
    :param a: Digit (float or integer)
    :param b: Digit (float or integer)
    :return: Sum of 2 digits
    """
    return a + b


if __name__ == '__main__':
    try:
        digit1 = int(sys.argv[1])
        digit2 = int(sys.argv[2])
        print(add(digit1, digit2))
    except Exception as error:
        print(f'Nie da się --- {error}')