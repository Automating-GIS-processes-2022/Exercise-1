#!/usr/bin/env python3


"""Test the submitted solutions for exercise 1, problem 4 of AutoGIS."""

import pytest

import shapely.geometry

from points_decorator import points


class Test_Exercise_1_Problem_4:
    @points(
        1.5,
        "The first task of problem 4 does not produce the correct results. "
        "Check whether `lines` is a list of `shapely.geometry.LineStrings` "
        " generated from `data`."
    )
    def test_problem4_task1(self, problem4):
        assert isinstance(problem4.lines, list)
        for line in problem4.lines:
            assert isinstance(line, shapely.geometry.LineString)
        assert len(problem4.lines) == len(problem4.data)

    @points(
        1,
        "Problem 4: the result of calculating `total_length` does not seem correct"
    )
    def test_problem4_task2(self, problem4):
        assert isinstance(problem4.total_length, float)
        assert round(problem4.total_length, 2) == pytest.approx(3148.57)

    @points(
        1,
        "Problem 4: revisit `create_od_lines()`, it does not work as expected"
    )
    def test_problem4_task3_create_od_lines(self, problem4):
        od_lines = problem4.create_od_lines(
            problem4.origin_points,
            problem4.destination_points,
        )
        assert isinstance(od_lines, list)
        for line in od_lines:
            assert isinstance(line, shapely.geometry.LineString)
        assert len(od_lines) == len(problem4.data)

    @points(
        1,
        "Problem 4: revisit `calculate_total_distance()`, it does not work as expected"
    )
    def test_problem4_task3_calculate_total_distance(self, problem4):
        lines = [
            shapely.geometry.LineString([(0, 0), (0, 10)]),
            shapely.geometry.LineString([(20, 20), (20, 40)]),
        ]
        total_length = problem4.calculate_total_distance(lines)
        assert total_length == 30

    @points(
        0.25,
        "Problem 4: the function `create_od_lines()` does not seem to "
        "have a docstring"
    )
    def test_problem4_task3_create_od_lines_docstring(self, problem4):
        assert problem4.create_od_lines.__doc__

    @points(
        0.25,
        "Problem 4: the function `calculate_total_distance()` does "
        "have a docstring"
    )
    def test_problem4_task3_calculate_total_distance_docstring(self, problem4):
        assert problem4.calculate_total_distance.__doc__
