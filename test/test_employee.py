from module.employee import Employee
import pytest


@pytest.fixture
def employee():
    employee = Employee('tom', 'green', 50000)
    return employee


def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 55000


def test_give_custom_raise(employee):
    employee.give_raise(6789)
    assert employee.salary == 56789
