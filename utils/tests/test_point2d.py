from pytest import mark

# Personal utilities
from bsoyka_aoc_utils.points import Point2D


@mark.parametrize(
    ("x", "y"), [(1, 3), (0, 0), (-2, 1), (-4, -1), (1.7, 3.5), (5, 6.4)]
)
def test_point2d_init(x: int | float, y: int | float):
    point = Point2D(1, 2)
    assert point.x == 1
    assert point.y == 2


@mark.parametrize(
    ("point1", "point2", "expected"),
    [
        (Point2D(10, 10), Point2D(0, 0), 20),
        (Point2D(-10, -10), Point2D(0, 0), 20),
        (Point2D(0, 0), Point2D(10, 10), 20),
        (Point2D(0, 0), Point2D(-10, -10), 20),
        (Point2D(5, 5), Point2D(5, 5), 0),
    ],
)
def test_point2d_int_distance_with_given_point(
    point1: Point2D, point2: Point2D, expected: int
):
    assert point1.distance(point2) == expected


@mark.parametrize(
    ("point", "expected"),
    [
        (Point2D(10, 10), 20),
        (Point2D(-10, -10), 20),
        (Point2D(0, 0), 0),
        (Point2D(5, 5), 10),
        (Point2D(3, 6), 9),
    ],
)
def test_point2d_int_distance_with_default_point(
    point: Point2D, expected: int
):
    assert point.distance() == expected


@mark.parametrize(
    ("point", "expected"),
    [
        (Point2D(10.1, 10.1), 20.2),
        (Point2D(-10.4, -10.4), 20.8),
        (Point2D(0.0, 0.0), 0.0),
        (Point2D(5.0, 5.0), 10.0),
        (Point2D(3.7, 5.3), 9.0),
    ],
)
def test_point2d_float_distance_with_default_point(
    point: Point2D, expected: float
):
    assert point.distance() == expected
