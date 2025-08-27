import module.my_functions as my_functions
import pytest
import time


def test_add():
    assert my_functions.add(1, 2) == 3


def test_add_strings():
    assert my_functions.add('hello ', 'world!') == 'hello world!'


def test_divide():
    assert my_functions.divide(10, 5) == 2


def test_add_number_string():
    with pytest.raises(TypeError):
        assert my_functions.add('a', 1)


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        assert my_functions.divide(10, 0)


@pytest.mark.parametrize('a, b, result', [
    (10, 20, 30),
    (30, 40, 70),
    (50, 60, 110),
])
def test_adding(a, b, result):
    addition = my_functions.add(a, b)
    assert addition == result


@pytest.mark.parametrize('a, b, result', [
    (10, 5, 2),
    (10, 10, 1),
    (20, 4, 5),
])
def test_divides(a, b, result):
    divided = my_functions.divide(a, b)
    assert divided == result


@pytest.mark.slow
def test_very_slow():
    time.sleep(2)
    assert my_functions.divide(10, 5) == 2


@pytest.mark.skip(reason='This feature is currently broken.')
def test_add_skip():
    assert my_functions.add(10, 20) == 30


@pytest.mark.xfail(reason='We know we cannot divide by zero and it fails.')
def test_divide_zero_broken():
    my_functions.divide(4, 0)
