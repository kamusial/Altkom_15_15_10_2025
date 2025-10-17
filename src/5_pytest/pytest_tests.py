from sqlalchemy.sql.sqltypes import NULLTYPE

from pytest_code import *

def test1():
    assert mnozenie(2, 5) == 10

def test2():
    assert mnozenie(22, 1) == 22

def test3():
    assert mnozenie(100, 1.1) == 110

def test4():
    assert mnozenie(0.5, 0.25) == 0.125

def test5():
    assert mnozenie(2, 'piesek') == 'piesekpiesek'

def test6():
    assert mnozenie(True, 3) == None




