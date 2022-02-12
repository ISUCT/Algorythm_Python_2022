"""
>>> import io, sys 
>>> sys.stdin = io.StringIO(chr(10).join([\
'ababbababa',\
'aba'\
]))
>>> find_substring()
0 5 7
"""

def get_hash(fullstring, substring):
    p = 31
    q = 2 ** 31 - 1
    m = 1
    s1hash = 0

    for i in substring[::-1]:
        s1hash += ord(i) * m
        m *= p
        s1hash %= q
        m %= q
    
    m = 1
    hash = 0
    for i in fullstring[:len(substring)][::-1]:
        hash += m * ord(i)
        m *= p
        hash %= q
        m %= q
    
    hashtag = 1
    for i in range(len(substring) - 1):
        hashtag *= p
        hashtag %= q
    
    List = []
    if hash == s1hash: List.append(0)
    for i in range(1, len(fullstring) - len(substring) + 1):
        hashnew = ((hash % q - ord(fullstring[i - 1]) * hashtag % q) * p % q + ord(fullstring[i + len(substring) - 1])) % q
        if hashnew == s1hash: 
            List.append(i)
        hash = hashnew
    return List

def find_substring(): 
    fullstring = str(input())
    substring = str(input())
    Arr = get_hash(fullstring,substring)
    print(' '.join(map(str, Arr)))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)