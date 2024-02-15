


def validate_age(age: object) -> object:
    # checks the value of age and raises a value error
    # if the age is below a certain threshold.

    # There are two scenarios here
    # When the age is less than zero
    # and When the age is greater than equal to zero.

    if age < 0:
        raise ValueError("Age cannot be less than 0")

