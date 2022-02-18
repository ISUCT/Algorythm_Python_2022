"""
>>> import io, sys
>>> sys.stdin = io.StringIO(chr(10).join([\
'5',\
'1 0 1 2 0'\
]))
>>> count_deferent()
3
"""

def count_deferent():
    int(input())
    x = len(set(map(int,input().split(" "))))
    print(x)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
