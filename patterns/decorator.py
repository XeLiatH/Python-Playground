# -*- coding: utf-8 -*-
"""
@author Matěj Beran
"""


def currency(func):
    def func_wrapper(*args, **kwargs):
        return str(func(*args, **kwargs)) + " Kč"
    return func_wrapper


@currency
def add(a, b):
    return a + b


def visual_test():
    print("{0}".format(add(10, 10)))


if __name__ == '__main__':
    visual_test()
