# -*- coding: utf-8 -*-
"""
@author Matěj Beran

Greatest Common Divisor (GCD)
---
Using the Euclid's algorithm
Can be called from command line
"""

import sys
import argparse


def gcd(a: int, b: int):
    r = a % b
    if r == 0:
        return b
    return gcd(b, r)


def gcd_multiple(numbers: list):
    num_len = len(numbers)
    # TODO: Ugh, don't think thi is cool
    if num_len == 1:
        return numbers[0]

    if num_len == 2:
        return gcd(numbers[0], numbers[1])

    _gcd = 1
    for i in range(num_len - 2):
        _gcd = gcd(numbers[i], gcd(numbers[i + 1], numbers[i + 2]))
    return _gcd


def parse_args(args):
    """
    Parses command line arguments
    """

    parser = argparse.ArgumentParser(
        description="Computes the greatest common divisor using the Euclidean algorithm")

    # TODO: would like to constraint nargs to 2 or more
    parser.add_argument('numbers', type=int, nargs='+',
                        help="Numbers to determine greates common divisor on")

    return parser.parse_args(args)


def handle_io(args):
    """
    Handles the input arguments of the program
    """

    parsed = parse_args(args)
    print(gcd_multiple(parsed.numbers))

    return 0


if __name__ == "__main__":
    handle_io(sys.argv[1:])
