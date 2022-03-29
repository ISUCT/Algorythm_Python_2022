'''
>>> import io, sys
>>> sys.stdin = io.StringIO(chr(10).join(['ababbababa','aba']))  # input
>>> find_substring()
0 5 7
'''

def get_hash(fullstring, substring):
    p, q, m = 31, 2 ** 31 - 1, 1
    subhash = 0
    curhash = 0
    hashtag = 1
    tags = []
    for i in substring[::-1]:
        subhash += ord(i) * m
        m *= p
        subhash %= q
        m %= q
    m = 1
    for i in fullstring[:len(substring)][::-1]:
        curhash += m * ord(i)
        m *= p
        curhash %= q
        m %= q
    for _ in range(len(substring) - 1):
        hashtag *= p
        hashtag %= q
    if curhash == subhash:
        tags.append(0)
    for i in range(1, len(fullstring) - len(substring) + 1):
        newhash = ((curhash % q - ord(fullstring[i - 1]) * hashtag % q) * p % q + ord(fullstring[i + len(substring) - 1])) % q
        if newhash == subhash:
            tags.append(i)
        curhash = newhash
    return tags

def find_substring():
    print(*get_hash(str(input()), str(input())))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)