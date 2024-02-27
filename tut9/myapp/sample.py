import requests

from tut9.myapp.dice import roll_dice


def guess_number(num):
    result = roll_dice()
    if num == result:
        return "You Won!"
    else:
        return "You Lost!"

# Some of the mock consideration, when writing the unit test for the function below.
# no internet.
# ip may change with time.
#
def get_ip():
    response = requests.get("https://httpbin.org/ip")
    if response.status_code == 200:
        return response.json()['origin']

