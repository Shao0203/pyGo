from module.shapes import Circle
import math
import pytest


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
