"""
>>> import io, sys 
>>> sys.stdin = io.StringIO(chr(10).join(['())(()']))
>>> get_psp()
2
>>> sys.stdin = io.StringIO(chr(10).join(['))(((']))
>>> get_psp()
5
"""

def get_psp():
    Counter = 0
    string = str(input())
    my_list = []
    for i in string:
        if (i == '('):
            my_list.append(i)
        elif (my_list != []) and (my_list[-1] == '('):
            my_list.pop()
        else:
            Counter += 1
    print(Counter+len(my_list))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
