import random
import time
import requests

def random_sum():
    a = random.randint(1,10) # range of values that randint can take.
    b = random.randint(1,7) # range of values that randint can take.
    return a + b
'''
Here we have to mock three parameters - Three different dependencies in a single unit test.
time.time
random.radint
request/response
'''
def silly():
    params = {
        "timestamp": time.time(),
        "number": random.randint(1,6)
    }
    response = requests.get("https://httpbin.org/ip", params)
    if response.status_code == 200:
        return response.json()['args']