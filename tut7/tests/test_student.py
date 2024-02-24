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

from tut7.myapp.student import Student, get_topper


# @pytest.fixture(scope="module")


# unit test to test the age of the student.
# Here we are using the fixture as the parameter to the function.

def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age



def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() ==20


def test_get_topper(make_dummy_student):
    students = [
        make_dummy_student("ram", 21),
        make_dummy_student("sham", 92),
        make_dummy_student("vam", 99)
    ]
    topper = get_topper(students)
    assert topper == students[2]

