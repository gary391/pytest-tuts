import sys

import pytest

from tut3.myapp.sample import add


# In order to skip a specific test we can use pytest markers.
@pytest.mark.skip(reason="Just wanna skip it!")
def test_add_num():
    assert add(1, 2) == 3


# Skip if the version of the python is greater than 3.7
@pytest.mark.skipif(sys.version_info > (3, 7), reason="You use python 3.7 or less")
def test_add_str():
    assert add("a", "b") == "ab"


# Here the test will be ignored as the test will raise some exception.
# xfail we are tell the pytest to ignore the test if it raises an exception.

# Here we can specify a condition which cause the failed test to be ignored by pytest.
@pytest.mark.xfail(sys.version_info > (3, 7), reason="don't run on python")
def test_add_num_list():
    assert add([1], [2]) == [1, 2]
    raise Exception()
