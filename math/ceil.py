# -*- coding: utf-8 -*-
"""
@author Matěj Beran
"""


def ceil(n):
    return n + (1 - (n % 1))


if __name__ == '__main__':
    print(ceil(20.5))
