#!/usr/bin/env python


"""Define fixtures shared among all tests."""


import pathlib
import pytest

from import_notebook import import_notebook


TESTS_PATH = pathlib.Path(__file__).absolute().parent
NOTEBOOKS_PATH = TESTS_PATH.parent


@pytest.fixture(scope="session")
def notebooks_path():
    yield NOTEBOOKS_PATH


@pytest.fixture(scope="session")
def problem1(notebooks_path):
    yield import_notebook(notebooks_path / "Exercise-1-problem-1-2.ipynb")


@pytest.fixture(scope="session")
def problem2(notebooks_path):
    yield import_notebook(notebooks_path / "Exercise-1-problem-1-2.ipynb")


@pytest.fixture(scope="session")
def problem3(notebooks_path):
    yield import_notebook(notebooks_path / "Exercise-1-problem-3-4.ipynb")


@pytest.fixture(scope="session")
def problem4(notebooks_path):
    yield import_notebook(notebooks_path / "Exercise-1-problem-3-4.ipynb")
