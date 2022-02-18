"""
>>> import io, sys 
>>> sys.stdin = io.StringIO(chr(10).join([\
'7 3',\
'1 3 2 4 5 3 1'\
]))
>>> get_minimums_on_segments()
1
2
2
3
1
"""

from collections import deque

def get_minimums_on_segments():
    deq = deque()
    length, len_wind = (int(i) for i in input().split())
    a = list(map(int,input().split()))
    for i in range(len_wind):
        while (deq) and (a[i] < a[deq[-1]]) :
            deq.pop()
        deq.append(i)

    for i in range(len_wind, length):
        print(a[deq[0]])

        while (deq) and (deq[0] <= i-len_wind):
            deq.popleft()
             
        while (deq) and (a[i] < a[deq[-1]]) :
            deq.pop()
        deq.append(i)

    print(a[deq[0]])

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
