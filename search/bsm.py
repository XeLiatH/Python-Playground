# -*- coding: utf-8 -*-
"""
@author Matěj Beran

Binary search method
---
Using interval halving to find a number in a sorted array (bisection)
"""

import datetime
import math


def bsm_search(number: int, data):
    index = math.floor(len(data) / 2)
    value = data[index]

    if index <= 0:
        return False
    if number == value:
        return True
    if number > value:
        return bsm_search(number, data[index:])
    if number < value:
        return bsm_search(number, data[:index])
    return False


def linear_search(number: int, data):
    for _ in data:
        if _ == number:
            return True
    return False


def visual_test():
    n = 799210
    d = range(1000000)

    print("\nLooking for %d" % n)
    print("Data length %d\n---" % len(d))

    print("\nBinary search\n---")
    one = datetime.datetime.now()
    print(bsm_search(n, d))
    diff = datetime.datetime.now() - one
    print("time[s]: " + str(diff.seconds))
    print("time[ms]: " + str(diff.microseconds))

    print("\nLinear search\n---")
    one = datetime.datetime.now()
    print(linear_search(n, d))
    diff = datetime.datetime.now() - one
    print("time[s]: " + str(diff.seconds))
    print("time[ms]: " + str(diff.microseconds))


if __name__ == "__main__":
    visual_test()
