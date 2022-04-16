'''
>>> import io, sys
>>> sys.stdin = io.StringIO(chr(10).join(['5', '0 0 2 0 1', '5', '1 5 2', '2 4 2', '3 5 3', '1 1 1', '3 4 1']))
>>> query_k()
2 4 -1 1 4
'''

def create_tree(it, v, le, ri, xs):
    if ri - le == 1:
        it[v] = xs[le]
        return
    m = (ri + le) // 2
    create_tree(it, 2 * v + 1, le, m, xs)
    create_tree(it, 2 * v + 2, m, ri, xs)
    it[v] = it[2 * v + 1] + it[2 * v + 2]

def search(it, v, le, ri, k):
    if k > it[v]:
        return -1
    if ri - le == 1:
        return ri
    m = (ri + le) // 2
    if it[2 * v + 1] >= k:
        return search(it, 2 * v + 1, le, m, k)
    else:
        return search(it, 2 * v + 2, m, ri, k - it[2 * v + 1])

def get_sum(it, v, le, ri, ql, qr):
    if ql <= le and qr >= ri:
        return it[v]
    if ql >= ri or qr <= le:
        return 0
    m = (ri + le) // 2
    return get_sum(it, 2 * v + 1, le, m, ql, qr) + get_sum(it, 2 * v + 2, m, ri, ql, qr)

def query_k():
    n = int(input())
    xs = [0 if int(i) != 0 else 1 for i in input().split()]
    it = [0] * 4 * n
    create_tree(it, 0, 0, n, xs)
    res = []
    q = int(input())
    while q != 0:
        le, ri, k = map(int, input().split())
        s = get_sum(it, 0, 0, n, le - 1, ri)
        if s >= k and le > 1:
            res.append(search(it, 0, 0, n, k + get_sum(it, 0, 0, n, 0, le - 1)))
        elif s >= k and le == 1:
            res.append(search(it, 0, 0, n, k))
        else:
            res.append(-1)
        q -= 1
    print(*res)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)