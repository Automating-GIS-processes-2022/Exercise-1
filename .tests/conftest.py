#!/usr/bin/env python


"""Define fixtures shared among all tests."""


import pathlib
import pytest


TESTS_PATH = pathlib.Path(__file__).absolute().parent
NOTEBOOKS_PATH = TESTS_PATH.parent


@pytest.fixture(scope="session")
def notebooks_path():
    yield NOTEBOOKS_PATH
