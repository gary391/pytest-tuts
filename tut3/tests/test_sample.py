import pytest

from tut3.myapp.sample import add


# In order to skip a specific test we can use pytest markes
@pytest.mark.skip
def test_add_num():
    assert add(1, 2) == 3


def test_add_str():
    assert add("a", "b") == "ab"


