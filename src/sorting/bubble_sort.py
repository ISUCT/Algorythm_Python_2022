"""
>>> import io, sys 
>>> sys.stdin = io.StringIO(chr(10).join(['4','4 3 2 1']))  # input
>>> bubble_sort()
3 4 2 1
3 2 4 1
3 2 1 4
2 3 1 4
2 1 3 4
1 2 3 4
>>> sys.stdin = io.StringIO(chr(10).join(['4','1 2 3 4']))  # input
>>> bubble_sort()
0
"""

def bubble_sort():
    n = int(input())
    inp_string = input()
    str_lst = inp_string.split(" ")
    int_lst = list(map(int, str_lst))
    changes_count = 0
    for i in range(n-1):
        for j in range(n-1-i):
            if int_lst[j] > int_lst[j+1]:
                int_lst[j],int_lst[j+1] = (int_lst[j+1],int_lst[j])
                changes_count += 1
                print(" ".join(map(str, int_lst)))  
    if changes_count == 0: 
        print(0)
    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)