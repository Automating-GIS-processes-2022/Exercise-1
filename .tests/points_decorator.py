#!/usr/bin/env python3


"""Decorates a test to report points as a `record_property’."""


import inspect


def points(points=0, error_message="", bonus_task=False):

    def _points(function):

        def wrapper(*args, **kwargs):
            record_property = kwargs.pop("record_property")
            record_property("points", points)
            record_property("error_message", error_message)
            record_property("bonus_task", bool(bonus_task))
            return function(*args, **kwargs)

        # add `record_property` to `wrapper`’s signature in a way
        # that makes pytest replace it with its built-in fixture
        # (cf. https://stackoverflow.com/q/65734222 )
        original_signature = inspect.signature(function)
        wrapper.__signature__ = inspect.signature(function).replace(
            parameters=(
                list(original_signature.parameters.values())
                + [
                    inspect.Parameter(
                        "record_property",
                        inspect.Parameter.POSITIONAL_OR_KEYWORD,
                    ),
                ]
            )
        )
        return wrapper
    return _points
