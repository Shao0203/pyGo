from module.shapes import Circle, Rectangle
import pytest
import math


def test_circle_area(circle):
    assert math.isclose(circle.area(), math.pi *
                        circle.radius ** 2, rel_tol=1e-5)


def test_circle_perimeter(circle):
    assert math.isclose(circle.perimeter(), 2 * math.pi *
                        circle.radius, rel_tol=1e-5)


def test_rectangle_area(rect):
    assert rect.area() == rect.length * rect.width


def test_rectangle_perimeter(rect):
    assert rect.perimeter() == 2 * (rect.length + rect.width)


@pytest.mark.parametrize('length, width, expected_area', [
    (2, 3, 6),
    (5, 5, 25),
    (10, 1, 10),
])
def test_rect_area(length, width, expected_area):
    rect = Rectangle(length, width)
    assert rect.area() == expected_area


@pytest.mark.parametrize('length, width, expected_perimeter', [
    (2, 3, 10),
    (5, 5, 20),
    (10, 1, 22),
])
def test_rect_perimeter(length, width, expected_perimeter):
    rect = Rectangle(length, width)
    assert rect.perimeter() == expected_perimeter


def test_rect_equal():
    rect1 = Rectangle(1, 2)
    rect2 = Rectangle(1, 2)
    assert rect1 == rect2


def test_rect_not_equal():
    rect1 = Rectangle(1, 2)
    rect2 = Rectangle(3, 4)
    assert rect1 != rect2


def test_rect_circle_compare(circle, rect):
    assert circle != rect
