"""
>>> import io, sys 
>>> sys.stdin = io.StringIO(chr(10).join(['z']))
>>> cyclic_string()
1
"""

def find_prefixes(string):
    length = len(string)
    prefixes = [0] * length

    for i in range(length - 1):
        j = prefixes[i]

        while (j > 0) and (string[i + 1] != string[j]):
            j = prefixes[j - 1]

        if string[i + 1] == string[j]:
            prefixes[i + 1] = j + 1
        else:
            prefixes[i + 1] = 0

    return prefixes

def find_period(string):
    prefixes = find_prefixes(string)

    length = len(string)
    result = length - prefixes[length - 1]

    if length % result == 0:
        return length // result

    return 1

def cyclic_string():
    string = input()
    result = find_period(string)

    print(result)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
