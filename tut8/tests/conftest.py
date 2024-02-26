from datetime import datetime

import pytest

from tut8.myapp.student import Student


# parameterize a fixture - For each parameter the unit test will be executed.
# Here we can provide Ids similar to pytest.marker (parameterization)

# @pytest.fixture(params=[21, 19], ids=["eligible", "ineligible"])
@pytest.fixture
# For consuming the parameter is done using the request fixture which is a build in fixture.
def dummy_student(request):
    return Student("Test", datetime(2000, 1, 1), "coe", request.param)



# fixture factory
@pytest.fixture
def make_dummy_student():
    # return a function

    def _make_dummy_student(name, credits):
        return Student(name, datetime(2000, 1, 1), 'coe', credits)

    return _make_dummy_student
