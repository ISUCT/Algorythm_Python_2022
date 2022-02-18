"""
>>> import io, sys 
>>> sys.stdin = io.StringIO(chr(10).join([\
'a',\
'b'\
]))
>>> cyclic_shift()
-1
>>> sys.stdin = io.StringIO(chr(10).join([\
'zabcd',\
'abcdz'\
]))
>>> cyclic_shift()
4
"""

def get_shift_size(first_string, second_string):
    if second_string == first_string:
        return 0

    second_string *= 2

    p = 13
    m = 1
    q = 2**31 - 1

    first_hash = 0
    second_hash = 0
    xt = 1

    for i in first_string[::-1]:
        first_hash = (first_hash + ord(i) * m) % q
        m = (m * p) % q

    m = 1
    for i in second_string[:len(first_string)][::-1]:
        second_hash = (second_hash + ord(i) * m) % q
        m = (m * p) % q

    for i in range(len(first_string) - 1):
        xt = (xt * p) % q

    for i in range(1, len(second_string) - len(first_string) + 1):
        if second_hash == first_hash:
            return i - 1

        second_hash = p * (second_hash - ord(second_string[i - 1]) * xt)
        second_hash += ord(second_string[i + len(first_string) - 1])
        second_hash %= q

    return -1


def cyclic_shift():
    first_string = input()
    second_string = input()

    result = get_shift_size(first_string, second_string)
    print(result)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
