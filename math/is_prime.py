# -*- coding: utf-8 -*-
"""
@author Matěj Beran
"""

import math


def is_prime(number: int):
    i = 2
    while i <= math.floor(math.sqrt(number)):
        if number % i == 0:
            return False
        i += 1
    return True


def visual_test():
    print(is_prime(6))


if __name__ == "__main__":
    visual_test()
