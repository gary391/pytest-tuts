from unittest import mock
from unittest.mock import call

from tut10.myapp.sample import random_sum
from tut10.myapp.sample import silly


@mock.patch("tut10.myapp.sample.random.randint")
def test_random_sum(mock_randint):
    # Using side effect you can pass multiple values
    # you can also pass exception as well.
    # and we can throw exception whereas return_value doesn't throw the exception.
    # Here in this example we are using side effect to pass two different values i.e. 3,4
    mock_randint.side_effect = [3, 4]
    assert random_sum() == 7
    # using has_calls we can test the range of values.
    mock_randint.assert_has_calls(calls=[call(1, 10), call(1, 7)])

@mock.patch("tut10.myapp.sample.random.randint")
@mock.patch("tut10.myapp.sample.time.time")
@mock.patch("tut10.myapp.sample.requests.get")
# The order of the mock object we get will start from the bottom.
def test_silly(mock_request_get, mock_time, mock_randint):
    test_params = {
        "timestamp": 123,
        "number": 5
    }
    mock_time.return_value = test_params["timestamp"]
    mock_randint.return_value = 5
    # mocking the get request
    mock_request_get.return_value = mock.Mock(**{"status_code" : 200, "json.return_value": {"args": test_params}})

    assert silly() == test_params
