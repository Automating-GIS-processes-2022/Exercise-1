#!/usr/bin/env python3


"""Test the submitted solutions for exercise 1, problem 3 of AutoGIS."""

import pytest

import pandas
import shapely.geometry

from points_decorator import points


class Test_Exercise_1_Problem_3:
    @points(
        1,
        "Problem 3: Did you read the correct data file into a "
        "`pandas.DataFrame` variable called `data`?"
    )
    def test_problem3_task1(self, problem3):
        assert isinstance(problem3.data, pandas.DataFrame)
        # assert problem3.data.shape == (14643, 13)  # changed in next step
        assert len(problem3.data) == 14643

    @points(
        1.5,
        "Problem 3: `data` does not (only) contain the four columns it should"
    )
    def test_problem3_task2(self, problem3):
        assert list(problem3.data.columns) == ["from_x", "from_y", "to_x", "to_y"]

    @points(
        2.5,
        "Problem 3: There’s something wrong with `destination_points` "
        "and/or `origin_points`"
    )
    def test_problem3_task3(self, problem3):
        for point_list in (problem3.origin_points, problem3.destination_points):
            assert isinstance(point_list, list)
            assert len(point_list) == len(problem3.data)
            for point in point_list:
                assert isinstance(point, shapely.geometry.Point)

        assert problem3.origin_points[0].x == pytest.approx(24.9704379)
        assert problem3.origin_points[0].y == pytest.approx(60.3119173)

        assert problem3.destination_points[0].x == pytest.approx(24.8560344)
        assert problem3.destination_points[0].y == pytest.approx(60.3999406)
