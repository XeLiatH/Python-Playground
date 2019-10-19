"""

Fibonacci test file
---

"""


import fib


def test_recursion_0():
    assert fib.fib_recursion(0) == 0


def test_recursion_1():
    assert fib.fib_recursion(1) == 1


def test_recursion_10():
    assert fib.fib_recursion(10) == 55


def test_memo_10():
    assert fib.fib_memo(10) == 55


def test_memo_0():
    assert fib.fib_memo(0) == 0


def test_memo_1():
    assert fib.fib_memo(1) == 1


def test_bottom_up_10():
    assert fib.fib_bottom_up(10) == 55


def test_bottom_up_0():
    assert fib.fib_bottom_up(0) == 0


def test_bottom_up_1():
    assert fib.fib_bottom_up(1) == 1
