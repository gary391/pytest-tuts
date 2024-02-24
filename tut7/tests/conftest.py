from datetime import datetime

import pytest

from tut7.myapp.student import Student


@pytest.fixture
def dummy_student():
    return Student("Test", datetime(2000, 1, 1), "coe", 20)


# fixture factory
@pytest.fixture
def make_dummy_student():
    # return a function

    def _make_dummy_student(name, credits):
        return Student(name, datetime(2000, 1, 1), 'coe', credits)

    return _make_dummy_student
