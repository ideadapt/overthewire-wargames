import re
import requests
from time import sleep

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

for line in open('languagecodes.txt'):
    print(line)
    resp = requests.get(f'https://kue.echo.olymp/assets/i18n/{line.strip()}.json', {}, verify=False)
    if resp.status_code == 200 and re.search(r'NAV_SEARCH', resp.text, flags=re.MULTILINE):
        print('------------------')
        print(line)
    sleep(0.2)
