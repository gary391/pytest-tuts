from unittest import mock

import pytest

from tut9.myapp.sample import get_ip
from tut9.myapp.sample import guess_number


# Whenever you patch an object, its corresponding mock object is returned as an argument.
# to your unit test.
@pytest.mark.parametrize("_input, expected", [(3, "You Won!"), (4, "You Lost!")])
@mock.patch("tut9.myapp.sample.roll_dice")
def test_guess_number(mock_roll_dice, _input, expected): # parameter are paced here after the mock object.
    mock_roll_dice.return_value = 3
    # We are passing two sets of parameters when the value is 3 and when it is 4
    # roll_dice value has been mocked to 3
    assert guess_number(_input) == expected
    mock_roll_dice.assert_called_once() # Mock object was called once.


@mock.patch("tut9.myapp.sample.requests.get")
def test_get_ip(mock_request_get):
    mock_request_get.return_value = mock.Mock(name="mock response", **{"status_code": 200, "json.return_value":{"origin":"0.0.0.0"}})

    assert get_ip() == "0.0.0.0"
    mock_request_get.assert_called_once_with("https://httpbin.org/ip")