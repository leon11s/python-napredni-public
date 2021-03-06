import os
from helpers.example_1 import example1

"""
This file (test_example1.py) contains the unit tests for the example1.py file.
"""


def test_get_current_directory(monkeypatch):
    """
    GIVEN a monkeypatched version of os.getcwd()
    WHEN example1() is called
    THEN check the current directory returned
    """

    def mock_getcwd():
        return "/data/user/directory123"

    monkeypatch.setattr(os, "getcwd", mock_getcwd)
    assert example1() == "/data/user/directory123"
