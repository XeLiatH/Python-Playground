# -*- coding: utf-8 -*-
"""
@author Matěj Beran
"""

from bubble import bubble


def test_default():
    assert bubble([20, 5, 6, 3, 25, 15]) == [3, 5, 6, 15, 20, 25]
