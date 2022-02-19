'''
>>> import io, sys
>>> sys.stdin = io.StringIO(chr(10).join([\
'1',\
'1'\
]))
>>> task_merge_sort()
1
>>> sys.stdin = io.StringIO(chr(10).join([\
'2',\
'3 1',\
]))
>>> task_merge_sort()
1 2 1 3
1 3
>>> sys.stdin = io.StringIO(chr(10).join([\
'5',\
'5 4 3 2 1',\
]))
>>> task_merge_sort()
1 2 4 5
4 5 1 2
3 5 1 3
1 5 1 5
1 2 3 4 5
>>> print(merge([2,3,4],[1,2,3]))
[1, 2, 2, 3, 3, 4]
'''

def merge(A, B):
    res = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
    while i < len(A):
        res.append(A[i])
        i += 1
    while j < len(B):
        res.append(B[j])
        j += 1
    return res

def merge_sort(A, begin, end):
    if (end - begin) == 1:
        return A[begin:end]
    middle = int((begin + end) / 2)
    left = merge_sort(A, begin, middle)
    right = merge_sort(A, middle, end)
    sort = merge(left, right)
    print(begin + 1, end, sort[0], sort[-1])
    return sort

def task_merge_sort():
    n = int(input())
    print(*merge_sort(list(map(int, input().split())), 0, n))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)