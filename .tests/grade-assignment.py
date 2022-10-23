#!/usr/bin/env python3


import contextlib
import json
import os
import pathlib

import pytest


TESTS_PATH = pathlib.Path(__file__).parent


class PointsCounter:
    def __init__(self):
        self.points = 0
        self.possible_points = 0
        self.error_messages = []
        self.bonus_tasks = 0

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        """
        Summarise the points awarded by each test.

        This function is called for each completed test.
        """
        outcome = yield
        report = outcome.get_result()
        if report.when == "call":
            user_properties = dict(report.user_properties)
            try:
                possible_points = user_properties["points"]
                error_message = user_properties["error_message"]
                bonus_task = user_properties["bonus_task"]

                self.possible_points += possible_points
                if report.outcome == "passed":
                    self.points += possible_points
                    if bonus_task:
                        self.bonus_tasks += 1
                else:
                    self.error_messages.append(error_message)
            except KeyError:
                pass


def format_feedback(student_username, points_counter):
    """
    Phrase and format feedback to the student.

    Arguments
    =========
    points_counter : PointsCounter
        A PointsCounter instance that has recorded the possible and actually
        gained points of a suite of pytest tests.

    Returns
    =======
    str : JSON-encoded feedback that can be used as environment variables in a
    Github `peter-evans/create-or-update-comment@v2` action (contains a ‘BODY’
    and a ’REACTION’ value)
    """
    points = points_counter.points
    possible_points = points_counter.possible_points
    bonus_tasks = points_counter.bonus_tasks
    error_messages = points_counter.error_messages

    percentage = float(points) / possible_points

    body = ""
    reaction = ""

    if points:
        body = (
            f"Great job, {student_username}!\n"
            "\n"
            "With the latest commit and push, your solution for the exercise "
            f"achieves {points:1.0f} points out of {possible_points:1.0f} "
            "possible points. \n"
            "\n"
        )
        if percentage < 1:
            body += (
                "Keep up the good work!\n\n"
            )
            reaction = "+1"

            if bonus_tasks:
                body += (
                    f"Congratulations also on completing {bonus_tasks:0.0f} "
                    f"optional task{'s' if bonus_tasks > 1 else ''}. "
                    "You got the hang of it!\n\n"
                )

            body += (
                "We noticed that the following things could still be improved:\n"
            )
            for error_message in error_messages:
                body += f"- {error_message}\n"

        else:
            body += (
                f"Amazing work! That’s full points! Well done!\n\n"
            )
            reaction = "hooray"

            if bonus_tasks:
                body += (
                    f"On top that, you also completed {bonus_tasks:0.0f} "
                    f"optional task{'s' if bonus_tasks > 1 else ''}. "
                    "Fantastic job!\n\n"
                )

    else:  # 0 points so far
        body = (
            "So far, your solution to the exercise "
            "has not gained any points.\n"
            "No worries: until the deadline, you can submit as many new "
            "versions as you want.\n\n"
            "If you feel stuck, don’t hesitate to come to the work sessions "
            "or post a question on Slack!"
        )

    feedback = json.dumps({
        "body": body,
        "reaction": reaction
    })
    return feedback


def main():
    points_counter = PointsCounter()

    # run pytest, but hide all of its output
    with open(os.devnull, "w") as devnull:
        with contextlib.redirect_stdout(devnull):
            with contextlib.redirect_stderr(devnull):
                pytest.main([TESTS_PATH], plugins=[points_counter])

    feedback = format_feedback(os.environ["STUDENT_USERNAME"], points_counter)
    print(f"FEEDBACK={feedback:s}")


if __name__ == "__main__":
    main()
