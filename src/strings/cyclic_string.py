'''
>>> import io, sys
>>> sys.stdin = io.StringIO('z')  # input
>>> cyclic_string()
1
'''

def find_prefs(string, length):
    prefs = [0] * length
    for i in range(length - 1):
        j = prefs[i]
        while (j > 0) and (string[i + 1] != string[j]):
            j = prefs[j - 1]
        if (string[i + 1] == string[j]):
            prefs[i + 1] = j + 1
        else:
            prefs[i + 1] = 0
    return prefs

def cyclic_string():
    string = list(str(input()))
    length = len(string)
    prefs = find_prefs(string, length)
    print(length - prefs[-1])

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)