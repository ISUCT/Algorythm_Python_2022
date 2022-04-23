'''
>>> import io, sys
>>> sys.stdin = io.StringIO(chr(10).join(['5', '2 2 2 1 5', '2', '2 3', '2 5']))
>>> query_NOD()
2 1
'''

from math import gcd

def create_tree(it, v, le, ri, xs):
    if ri - le == 1:
        it[v] = xs[le]
        return
    m = (ri + le) // 2
    create_tree(it, 2 * v + 1, le, m, xs)
    create_tree(it, 2 * v + 2, m, ri, xs)
    it[v] = gcd(it[2 * v + 1], it[2 * v + 2])

def get_NOD(it, v, le, ri, ql, qr):
    if ql <= le and qr >= ri:
        return it[v]
    if ql >= ri or qr <= le:
        return 0
    m = (ri + le) // 2
    tl = get_NOD(it, 2 * v + 1, le, m, ql, qr)
    tr = get_NOD(it, 2 * v + 2, m, ri, ql, qr)
    return gcd(tl, tr)

def query_NOD():
    n = int(input())
    xs = list(map(int, input().split()))
    it = [0] * 4 * n
    create_tree(it, 0, 0, n, xs)
    res = []
    q = int(input())
    while q != 0:
        le, ri = map(int, input().split())
        res.append(get_NOD(it, 0, 0, n, le - 1, ri))
        q -= 1
    print(*res)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)