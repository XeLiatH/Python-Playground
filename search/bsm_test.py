"""

Binary search method test file
---

"""

import bsm


def test_contains():
    assert bsm.bsm_search(2, [1, 2, 3, 4, 5]) == True


def test_does_not_contain():
    assert bsm.bsm_search(10, [1, 2, 3, 4, 5]) == False
