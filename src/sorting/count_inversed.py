"""
>>> import io, sys
>>> sys.stdin = io.StringIO(chr(10).join([\
'2',\
'3 1'\
]))
>>> count_inversed()
1
"""

def Sort(Arr, Num):
    List = [0]*Num
    return merge_sort(Arr, List, 0, Num-1)
 
def merge_sort(Arr, List, left, right):
    Counter = 0
    if left < right:
        mid = (left + right)//2
        Counter += merge_sort(Arr, List, left, mid)
        Counter += merge_sort(Arr, List, mid + 1, right)
        Counter += Merge(Arr, List, left, mid, right)
    return Counter
 
def Merge(Arr, List, left, mid, right):
    i = left     
    j = mid + 1 
    k = left     
    Counter = 0
    while i <= mid and j <= right:
        if Arr[i] <= Arr[j]:
            List[k] = Arr[i]
            k += 1
            i += 1
        else:
            List[k] = Arr[j]
            Counter += (mid-i + 1)
            k += 1
            j += 1
    while i <= mid:
        List[k] = Arr[i]
        k += 1
        i += 1
    while j <= right:
        List[k] = Arr[j]
        k += 1
        j += 1
    for now in range(left, right + 1):
        Arr[now] = List[now]    
    return Counter

def count_inversed():
    int(input())
    Arr = list(map(int, input().split()))
    Num = len(Arr)
    Arr = Sort(Arr, Num)
    print(Arr)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
