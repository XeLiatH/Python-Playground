# -*- coding: utf-8 -*-
"""
@author Matěj Beran
"""

from floor import floor


def test_default():
    assert floor(20.1) == 20.0
    assert floor(20.6) == 20.0
