# -*- coding: utf-8 -*-
"""
@author Matěj Beran
"""


from is_prime import is_prime


def test_default():
    assert is_prime(11) == True
    assert is_prime(5) == True
    assert is_prime(30) == False
    assert is_prime(17) == True
    assert is_prime(6) == False
    assert is_prime(10) == False
