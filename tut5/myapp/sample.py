import json

def save_dict(_dict, filepath):
    """
    The function take two parameters one is a dictionary and other one
    is a file path, saved the content of the dictionary as a json
    object at the file path and prints "saved".
    :param _dict:
    :param filepath:
    :return: None
    """
    json.dump(_dict, open(filepath, 'w'))
    print("saved")

"""
Write unit test for the above method:
1. Write a unit test to check if the file at the filepath was created or not.
2. Where do you create the file to validate the test.

Thus in this case we can use the pytest fixtures that provide temp directory. 
"""