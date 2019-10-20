# -*- coding: utf-8 -*-
"""
@author Matěj Beran
"""

from ceil import ceil


def test_default():
    assert ceil(20.1) == 21.0
    assert ceil(20.6) == 21.0
