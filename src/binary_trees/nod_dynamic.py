'''
>>> import io, sys
>>> sys.stdin = io.StringIO(chr(10).join(['5', '2 8 4 16 12', '5', 's 1 5', 's 4 5', 'u 3 32', 's 2 5', 's 3 3']))
>>> query_NOD()
2 4 4 32
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

def up(it, v, le, ri, ix, va):
    if ri - le == 1:
        it[v] = va
        return
    m = (ri + le) // 2
    if ix < m:
        up(it, 2 * v + 1, le, m, ix, va)
    else:
        up(it, 2 * v + 2, m, ri, ix, va)
    it[v] = gcd(it[2 * v + 1], it[2 * v + 2])

def query_NOD():
    n = int(input())
    it = [0] * 4 * n
    xs = list(map(int, input().split()))
    create_tree(it, 0, 0, n, xs)
    res = []
    q = int(input())
    while q != 0:
        que, le, ri = map(str, input().split())
        le, ri = int(le), int(ri)
        if que == 's':
            res.append(get_NOD(it, 0, 0, n, le - 1, ri))
        else:
            up(it, 0, 0, n, le - 1, ri)
        q -= 1
    print(*res)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)