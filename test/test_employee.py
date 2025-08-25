import pytest
from module.employee import Employee


@pytest.fixture
def employee():
    return Employee('Bright', 'Shao', 100000)


def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 105000


def test_give_custom_raise(employee):
    employee.give_raise(8000)
    assert employee.salary == 108000
