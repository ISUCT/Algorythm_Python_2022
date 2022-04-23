'''
>>> import io, sys
>>> sys.stdin = io.StringIO('())(()')
>>> find_psp()
2
>>> sys.stdin = io.StringIO('))(((')
>>> find_psp()
5
'''

def psp(string):
    arr = []
    count = 0
    for i in string:
        if i == '(':
            arr.append(i)
        elif arr != [] and arr[-1] == '(':
            arr.pop()
        else:
            count += 1
    return count + len(arr)

def find_psp():
    print(psp(str(input())))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)