import module.my_functions as my_functions
import pytest


def test_add():
    assert my_functions.add(1, 2) == 3


def test_add_strings():
    assert my_functions.add('hello ', 'world!') == 'hello world!'


def test_add_number_string():
    with pytest.raises(TypeError):
        assert my_functions.add('a', 1)


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        assert my_functions.divide(10, 0)


def test_divide():
    assert my_functions.divide(10, 5) == 2
