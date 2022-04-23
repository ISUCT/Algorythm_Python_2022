'''
>>> import io, sys
>>> sys.stdin = io.StringIO(chr(10).join(['1', '1']))
>>> inversions_count()
0
>>> sys.stdin = io.StringIO(chr(10).join(['2', '3 1']))
>>> inversions_count()
1
>>> sys.stdin = io.StringIO(chr(10).join(['5', '5 4 3 2 1']))
>>> inversions_count()
10
'''

def inversions_count():
    inversions = 0
    n = int(input())
    xs = list(map(int, input().split()))
    for i in range(n):
        for j in range(i + 1, n):
            if xs[i] > xs[j]:
                inversions += 1
    print(inversions)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)