from module.shapes import Circle, Rectangle
import pytest
import math


class TestCircle:
    # class-based, setup and teardown methods
    def setup_method(self, a):
        print(f'Setting up {a}')
        self.circle = Circle(10)

    def teardown_method(self, a):
        print(f'Teardown {a}')
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius


@pytest.fixture
def circle():
    return Circle(1)


@pytest.fixture
def rect():
    return Rectangle(5, 6)


def test_circle_area(circle):
    assert math.isclose(circle.area(), math.pi, rel_tol=1e-5)


def test_circle_perimeter(circle):
    assert math.isclose(circle.perimeter(), 2 * math.pi, rel_tol=1e-5)


def test_rectangle_area(rect):
    assert rect.area() == rect.width * rect.height


def test_rectangle_perimeter(rect):
    assert rect.perimeter() == 2 * (rect.width + rect.height)
