"""
To use the pytest fixture all you need to do is to pass a parameter to your
test with the same as the fixture.

"""
import json
import os

from tut5.myapp.sample import save_dict


def test_save_dict(tmpdir, capsys):
    filepath = os.path.join(tmpdir, "test.json")
    _dict = {"a": 1, "b": 2}

    save_dict(_dict, filepath)
    # Once the function is run usnig the parameter
    # assert up opening & reading the file contains the dictionary items.
    assert json.load(open(filepath, 'r')) == _dict

# For checking if saved value was printed our not.
# Using capsys and capfd
    # we need a new line at the end of saved as print adds a new line character.
    assert capsys.readouterr().out  == 'saved\n'