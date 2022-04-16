'''
>>> import io, sys
>>> sys.stdin = io.StringIO(chr(10).join(['3', '101 80', '305 90', '200 14']))
>>> pair_sort()
305 90
101 80
200 14
>>> sys.stdin = io.StringIO(chr(10).join(['3', '20 80', '30 90', '25 90']))
>>> pair_sort()
25 90
30 90
20 80
'''

def compare(A, B):
    if A[1] > B[1]:
        return True
    elif A[1] == B[1]:
        return A[0] < B[0]
    else:
        return False

def pair_sort():
    xs = []
    n = int(input())
    for _ in range(n):
        xs.append(list(map(int, input().split())))
    for i in range(len(xs)):
        x = xs[i]
        j = i - 1
        while j >= 0 and compare(x, xs[j]):
            xs[j + 1] = xs[j]
            j -= 1
        xs[j + 1] = x
    for x in xs:
        print(*x)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)