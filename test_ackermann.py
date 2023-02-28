
import ackermann
import math

depth = 40

def test_ADD():
    for x in range(0, depth):
        for y in range(0, depth):
            assert ackermann.MULT(x,y) == x * y

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