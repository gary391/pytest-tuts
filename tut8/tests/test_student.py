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

from tut8.myapp.student import is_eligible_for_degree


# @pytest.fixture(scope="module")


# unit test to test the age of the student.
# Here we are using the fixture as the parameter to the function.
# The unit test below using a dummy_student fixture which has two parameter.
# The unit test will be executed for two values i.e. 19 and 21 which are being passed from the
# dummy_student fixture.

def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age


def test_student_is_eligible_for_degree_false(make_dummy_student):
    assert is_eligible_for_degree(make_dummy_student('sam', 19)) is False


def test_student_is_eligible_for_degree_true(make_dummy_student):
    assert is_eligible_for_degree(make_dummy_student('sam', 21)) is True

# Here the credits, expected is the arguments and (19, False), (21, True) are the parameters.
# Paramterization of the unit test.
# When you are using paramterized fixture and marker, the fixture is first and then the parameters.
# Using this single test we are able to accomplish the same as we did with the two test above.
# Note here we will have to use fixture factory as a single fixture (dummy_student) object can't be parameterized
# As it is not a function but a direct value.

@pytest.mark.parametrize("credits,expected", [(19, False), (21, True)])
def test_student_is_eligible_for_degree(make_dummy_student, credits, expected):
    assert is_eligible_for_degree(make_dummy_student('sam', credits)) is expected

# Here another way to achieve the same as above with only the fixture, and not using the fixture factory.

# We need to connect the unit test parameters with the fixture parameters.
# You can provide fixture as a parameter using the indirect parameter.
# providing the name of the parameters which should be treated as fixtures.
@pytest.mark.parametrize("dummy_student,expected", [(19, False), (21, True)],
                         indirect=["dummy_student"])
def test_student_is_eligible_for_degree(dummy_student, expected):
    assert is_eligible_for_degree(dummy_student) is expected
