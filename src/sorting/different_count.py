'''
>>> import io, sys
>>> sys.stdin = io.StringIO(chr(10).join(['5','1 0 1 2 0']))  # input
>>> different_count()
3
'''

def different_count():
    n = int(input())
    print(len(set(map(int, input().split()))))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)