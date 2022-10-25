#!/usr/bin/env python3


"""Test the submitted solutions for exercise 1, problem 2 of AutoGIS."""

import pytest

import shapely.geometry

from points_decorator import points


class Test_Exercise_1_Problem_2:
    @points(0.9, "Problem 2: Something’s not quite right with `get_centroid()`.")
    def test_get_centroid(self, problem2):
        polygon = shapely.geometry.Polygon(
            [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
        )
        centroid = problem2.get_centroid(polygon)
        assert centroid == shapely.geometry.Point(0.5, 0.5)

    @points(0.66, "Problem 2: Does `get_centroid()` check its input?")
    def test_get_centroid_check_input(self, problem2):
        with pytest.raises(AssertionError):
            _ = problem2.get_centroid("NOT A SHAPELY GEOMETRY")

    @points(0.9, "Problem 2: `get_area()` does not seem to work 100%.")
    def test_get_area(self, problem2):
        polygon = shapely.geometry.Polygon(
            [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
        )
        area = problem2.get_area(polygon)
        assert area == 1

    @points(0.67, "Problem 2: `get_area()` should check that its input as a Polygon")
    def test_get_area_check_input(self, problem2):
        with pytest.raises(AssertionError):
            point = shapely.geometry.Point(1, 2)
            _ = problem2.get_area(point)

    @points(0.9, "Problem 2: Take another look at `get_length()`")
    def test_get_length(self, problem2):
        line = shapely.geometry.LineString([(0, 0), (1, 0)])
        length = problem2.get_length(line)
        assert length == 1
        polygon = shapely.geometry.Polygon(
            [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]
        )
        length = problem2.get_length(polygon)
        assert length == 4

    @points(0.67, "Problem 2: Make sure that `get_length()` checks its inputs.")
    def test_get_length_check_input(self, problem2):
        with pytest.raises((AssertionError, ValueError)):
            point = shapely.geometry.Point(1, 2)
            _ = problem2.get_length(point)

    @points(bonus_task=True)
    def test_get_length_check_input_raise_ValueError_exception(self, problem2):
        with pytest.raises(ValueError):
            point = shapely.geometry.Point(1, 2)
            _ = problem2.get_length(point)
