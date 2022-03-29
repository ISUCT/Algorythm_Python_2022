'''
>>> import io, sys
>>> sys.stdin = io.StringIO(chr(10).join(['1','1']))  # input
>>> task_merge_sort_count()
0
>>> sys.stdin = io.StringIO(chr(10).join(['2','3 1']))  # input
>>> task_merge_sort_count()
1
>>> sys.stdin = io.StringIO(chr(10).join(['5','5 4 3 2 1']))  # input
>>> task_merge_sort_count()
10
'''

def merge(A, B):
    res = []
    i = j = 0
    inversions = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
            inversions += (len(A) - i)
    res += A[i:]
    res += B[j:]
    return res, inversions

def merge_sort_count(A):
    if len(A) <= 1:
        return A, 0
    middle = int(len(A) / 2)
    left, inversions_left = merge_sort_count(A[:middle])
    right, inversions_right = merge_sort_count(A[middle:])
    merged, inversions = merge(left, right)
    inversions += inversions_left + inversions_right
    return merged, inversions

def task_merge_sort_count():
    n = int(input())
    print(merge_sort_count(list(map(int, input().split())))[1])

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)