# -*- coding: utf-8 -*-
"""
@author Matěj Beran
"""

from round import round


def test_default():
    assert round(20.1) == 20.0
    assert round(20.6) == 21.0
