# -*- coding: utf-8 -*-
"""
@author Matěj Beran
"""

from floor import floor
from ceil import ceil


def round(n):
    a = floor(n)
    b = n - a
    if b > 0.5:
        return ceil(n)
    return a


def visual_test():
    print(round(20.6))  # 21.0
    print(round(20.3))  # 20.0


if __name__ == '__main__':
    visual_test()
