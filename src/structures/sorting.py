'''
>>> import io, sys
>>> sys.stdin = io.StringIO(chr(10).join(['3', '3 2 1']))
>>> sort_ways()
YES
>>> sys.stdin = io.StringIO(chr(10).join(['4', '4 1 3 2']))
>>> sort_ways()
YES
>>> sys.stdin = io.StringIO(chr(10).join(['3', '2 3 1']))
>>> sort_ways()
NO
'''

def sort_ways():
    n = int(input())
    A = list(map(int, input().split()))
    B = []
    tmp = []
    a_sorted = sorted(A)
    for _ in range(n):
        if tmp == [] or tmp[-1] > A[0]:
            tmp.append(A[0])
            A.pop(0)
        else:
            while tmp != [] and tmp[-1] < A[0]:
                B.append(tmp[-1])
                tmp.pop(-1)
            if tmp == [] or tmp[-1] > A[0]:
                tmp.append(A[0])
                A.pop(0)
    if tmp != []:
        for _ in range(len(tmp)):
            B.append(tmp[-1])
            tmp.pop(-1)
    print('YES' if B == a_sorted else 'NO')

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)