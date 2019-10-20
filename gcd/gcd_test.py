# -*- coding: utf-8 -*-
"""
@author Matěj Beran
"""

import gcd


def test_default():
    assert gcd.gcd(10, 10) == 10


def test_same():
    assert gcd.gcd(10, 5) == gcd.gcd(10, 5)


def test_constant():
    c = 5
    assert c * gcd.gcd(10, 5) == gcd.gcd(c * 10, c * 5)


def test_impersonal():
    assert gcd.gcd(7, 11) == 1


def test_multiple():
    assert gcd.gcd_multiple([10, 20, 30]) == 10
