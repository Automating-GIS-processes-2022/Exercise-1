#!/usr/bin/env python3


"""Test the submitted solutions for exercise 1, problem 2 of AutoGIS."""

import pytest

import shapely.geometry

from points_decorator import points
from import_notebook import import_notebook


exercise1 = import_notebook("Exercise-1-problem-1-2.ipynb")


class Test_Exercise_1_Problem_2:
    @points(1, "Something’s not quite right with `get_centroid()`.")
    def test_get_centroid(self):
        polygon = shapely.geometry.Polygon(
            [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
        )
        centroid = exercise1.get_centroid(polygon)
        assert centroid == shapely.geometry.Point(0.5, 0.5)

    @points(0.66, "Does `get_centroid()` check its input?")
    def test_get_centroid_check_input(self):
        with pytest.raises(AssertionError):
            _ = exercise1.get_centroid("NOT A SHAPELY GEOMETRY")

    @points(1, "`get_area()` does not seem to work 100%.")
    def test_get_area(self):
        polygon = shapely.geometry.Polygon(
            [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
        )
        area = exercise1.get_area(polygon)
        assert area == 1

    @points(0.67, "`get_area()` should check that its input as a Polygon")
    def test_get_area_check_input(self):
        with pytest.raises(AssertionError):
            point = shapely.geometry.Point(1, 2)
            _ = exercise1.get_area(point)

    @points(1, "Take another look at `get_length()`")
    def test_get_length(self):
        line = shapely.geometry.LineString([(0, 0), (1, 0)])
        length = exercise1.get_length(line)
        assert length == 1
        polygon = shapely.geometry.Polygon(
            [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
        )
        length = exercise1.get_length(polygon)
        assert length == 4

    @points(0.67, "Make sure that `get_length()` checks its inputs.")
    def test_get_length_check_input(self):
        with pytest.raises((AssertionError, ValueError)):
            point = shapely.geometry.Point(1, 2)
            _ = exercise1.get_length(point)

    @points(bonus_task=True)
    def test_get_length_check_input_raise_ValueError_exception(self):
        with pytest.raises(ValueError):
            point = shapely.geometry.Point(1, 2)
            _ = exercise1.get_length(point)
