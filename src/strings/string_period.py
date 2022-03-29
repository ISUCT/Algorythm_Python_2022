'''
>>> import io, sys
>>> sys.stdin = io.StringIO('aaaaa')  # input
>>> string_period()
5
>>> sys.stdin = io.StringIO('abcabcabc')  # input
>>> string_period()
3
>>> sys.stdin = io.StringIO('abab')  # input
>>> string_period()
2
'''

def find_prefs(string, length):
    prefs = [0] * length
    prefs[0] = 0
    for i in range(length - 1):
        j = prefs[i]
        while (j > 0) and (string[i + 1] != string[j]):
            j = prefs[j - 1]
        if (string[i + 1] == string[j]):
            prefs[i + 1] = j + 1
        else:
            prefs[i + 1] = 0
    return prefs

def find_period(string):
    length = len(string)
    prefs = find_prefs(string, length)
    result = length - prefs[length - 1]
    if (length % result == 0):
        return length // result
    return 1

def string_period():
    print(find_period(list(str(input()))))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)