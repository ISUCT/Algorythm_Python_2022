'''
>>> import io, sys
>>> sys.stdin = io.StringIO(chr(10).join(['4', '4 3 2 1']))
>>> bubble_sort()
3 4 2 1
3 2 4 1
3 2 1 4
2 3 1 4
2 1 3 4
1 2 3 4
'''

def bubble_sort():
    n = int(input())
    xs = list(map(int, input().split()))
    swaps = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if xs[j] > xs[j + 1]:
                xs[j], xs[j + 1] = (xs[j + 1], xs[j])
                swaps += 1
                print(*xs)
    if swaps == 0:
        print(0)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
