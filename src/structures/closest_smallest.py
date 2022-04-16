'''
>>> import io, sys
>>> sys.stdin = io.StringIO(chr(10).join(['10', '1 2 3 2 1 4 2 5 3 1']))
>>> find_closest_smallest()
-1 4 3 4 -1 6 9 8 9 -1
'''

def find_closest_smallest():
    n = int(input())
    a = list(zip(list(map(int, input().split())), range(n)))
    tmp = []
    res = [0] * n
    for i in reversed(a):
        while tmp != [] and tmp[-1][0] >= i[0]:
            tmp.pop()
        if tmp == []:
            res[i[1]] = -1
        else:
            res[i[1]] = tmp[-1][1]
        tmp.append(i)
    print(*res)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)