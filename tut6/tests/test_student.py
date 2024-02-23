"""
Using fixture we can create a dummy student object,
so that we don't have to create the object again and again

Use of fixture scope:
- By default the scope of the pytest fixture is function which means the
 pytest fixture is recreated for each function. so by default the dummy_fixture
 is created three times, i.e. whenever the test function is run.

- Note: The side effect of using fixture other than function can create dependency
between the unit test which may not be desired.

"""
from datetime import datetime

import pytest

from tut6.myapp.student import Student


# @pytest.fixture(scope="module")
@pytest.fixture
def dummy_student():
    print("making dummy student")
    return Student("Test", datetime(2000, 1, 1), "coe")


# unit test to test the age of the student.
# Here we are using the fixture as the parameter to the function.

def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age


def test_student_add_credits(dummy_student):
    dummy_student.add_credits(5)
    assert dummy_student.get_credits() == 5

#
def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() ==0
