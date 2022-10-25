#!/usr/bin/env python3


"""Test the submitted solutions for exercise 1, problem 1+2 of AutoGIS."""


from points_decorator import points


class Test_Exercise_1_Problem_1_2_docstrings:
    @points(0.1, "Problem 1: `create_point_geometry` does not have a docstring")
    def test_docstrings_create_point_geometry(self, problem1):
        assert problem1.create_point_geometry.__doc__

    @points(0.1, "Problem 1: `create_line_geometry` does not have a docstring")
    def test_docstrings_create_line_geometry(self, problem1):
        assert problem1.create_line_geometry.__doc__

    @points(0.1, "Problem 1: `create_polygon_geometry` does not have a docstring")
    def test_docstrings_create_polygon_geometry(self, problem1):
        assert problem1.create_polygon_geometry.__doc__

    @points(0.1, "Problem 2: `get_centroid` does not have a docstring")
    def test_docstrings_get_centroid(self, problem2):
        assert problem2.get_centroid.__doc__

    @points(0.1, "Problem 2: `get_area` does not have a docstring")
    def test_docstrings_get_area(self, problem2):
        assert problem2.get_area.__doc__

    @points(0.1, "Problem 2: `get_length` does not have a docstring")
    def test_docstrings_get_length(self, problem2):
        assert problem2.get_length.__doc__
