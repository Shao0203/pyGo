import pytest
import math
from module.shapes import Circle, Rectangle


@pytest.fixture(params=[10, 20, 30])
def circle(request):
    radius = request.param
    return Circle(radius)


def test_circle_area(circle):
    assert math.isclose(circle.area(), math.pi *
                        circle.radius ** 2, rel_tol=1e-5)


def test_circle_perimeter(circle):
    assert circle.perimeter() == math.pi * circle.radius * 2


@pytest.mark.parametrize('length, width, expected_area', [
    (3, 2, 6), (5, 5, 25), (10, 1, 10)
])
def test_rectangle_area(length, width, expected_area):
    rect = Rectangle(length, width)
    assert rect.area() == expected_area


@pytest.mark.parametrize('length, width, expected_perimeter', [
    (3, 2, 10), (5, 5, 20), (10, 1, 22)
])
def test_rectangle_perimeter(length, width, expected_perimeter):
    rect = Rectangle(length, width)
    assert rect.perimeter() == expected_perimeter
