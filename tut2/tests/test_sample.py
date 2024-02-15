
import pytest

from tut2.myapp.sample import validate_age

# Using valid age - no exception is raised
def test_validate_age_valid_age():
    validate_age(10)

# Using invalid age - validate if the same exception is raised
# As mentioned in the script.

def test_validate_age_invalid_age():
    # Using with context we are raising a valueError.
    # pytest.raises returns an object of class Exception_info
    # Which contains all the information about the exception.
    with pytest.raises(ValueError) as exc_info:
        validate_age(-1)
        # How to validate if the correct message was printed when the exception was raised.
    assert str(exc_info.value) == "Age cannot be less than 0"

# using a match functionality in-build in pytest.

def test_validate_age_invalid_age_using_match():
    # Using with context we are raising a valueError
    # pytest.raises returns an object of class Exception_info
    # Which contains all the information about the exception.
    with pytest.raises(ValueError, match="Age cannot be less than 0"):
        validate_age(-1)
