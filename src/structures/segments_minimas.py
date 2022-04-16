'''
>>> import io, sys
>>> sys.stdin = io.StringIO(chr(10).join(['7 3', '1 3 2 4 5 3 1']))
>>> find_minimas()
1
2
2
3
1
'''

from collections import deque

def find_minimas():
    n, k = (int(i) for i in input().split())
    a = list(map(int, input().split()))
    d = deque()
    for i in range(k):
        while d and (a[i] < a[d[-1]]):
            d.pop()
        d.append(i)
    for i in range(k, n):
        print(a[d[0]])
        while d and (d[0] <= i - k):
            d.popleft()
        while d and (a[i] < a[d[-1]]):
            d.pop()
        d.append(i)
    print(a[d[0]])

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)