"""
>>> import io, sys 
>>> sys.stdin = io.StringIO(chr(10).join([\
'aaaaa'\
]))
>>> row_period()
5
>>> sys.stdin = io.StringIO(chr(10).join([\
'abcabcabc'\
]))
>>> row_period()
3
>>> sys.stdin = io.StringIO(chr(10).join([\
'abab'\
]))
>>> row_period()
2
"""

from cyclic_string import find_period

def row_period():
    print(find_period(input()))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
