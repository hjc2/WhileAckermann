
import ackermann
import math

depth = 40

def test_ADD():
    for x in range(0, depth):
        for y in range(0, depth):
            assert ackermann.ADD(x,y) == x + y

def test_MULT():
    for x in range(0, depth):
        for y in range(0, depth):
            assert ackermann.MULT(x,y) == x * y

def test_SUB():
    for x in range(0, depth):
        for y in range(0, depth):
            assert ackermann.SUB(x,y) == max(0, x - y)

def test_DIV():
    for x in range(0, depth):
        for y in range(1, depth):
            assert ackermann.DIV(x,y) == x // y

def test_MOD():
    for x in range(0, depth):
        for y in range(1, depth):
            assert ackermann.MOD(x,y) == x % y

def test_MVALUE():
    for x in range(0, depth):
        for y in range(1, depth):
            assert ackermann.MVALUE(x) == math.pow(10, len(str(x)))

def test_EMPTY():
    assert ackermann.EMPTY(1) == 0
    assert ackermann.EMPTY(0) == 0

    assert ackermann.EMPTY(10) == 1
    assert ackermann.EMPTY(101) == 1

def test_ACK():
    assert ackermann.ACK(1,1) == 3
    assert ackermann.ACK(2,2) == 7
    assert ackermann.ACK(1,5) == 7
    # assert ackermann.ACK(3,3) == 61

def A(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return A(m - 1, 1)
    else:
        return A(m - 1, A(m, n - 1))
