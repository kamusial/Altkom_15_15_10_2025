from joblib.testing import fixture
from kod import fizzbuss

def test1():
    assert fizzbuss(1) == 1

def test2():
    assert fizzbuss(2) == 2

def test3():
    assert fizzbuss(3) == 'fizz'

def test4():
    assert fizzbuss(5) == 'buzz'

def test5():
    assert fizzbuss(15) == 'fizzbuzz'

def test6():
    assert fizzbuss(0) == 0

def test7():
    assert fizzbuss(-5)

def test8():
    assert fizzbuss(5.2)

def test9():
    assert fizzbuss(5.8)

def test10():
    assert fizzbuss('five')

def test11():
    assert fizzbuss('5')
