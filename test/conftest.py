from module.shapes import Circle, Rectangle
import pytest


@pytest.fixture(scope='session', params=[1, 2, 3])
def circle(request):
    radius = request.param
    return Circle(radius)


@pytest.fixture(params=[(2, 3), (5, 5), (10, 1)])
def rect(request):
    length, width = request.param
    return Rectangle(length, width)
