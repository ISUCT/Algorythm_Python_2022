"""
>>> import io, sys
>>> sys.stdin = io.StringIO(chr(10).join([\
'5',\
'5 4 3 2 1'\
]))
>>> hoare_sort()
1 2 3 4 5
"""

def hoare_sort():
    n = int(input())
    inp_string = input()
    input_array = list(map(int, inp_string.split(" ")))
    
    counter = 1
    while counter < len(input_array):
        for i in range(len(input_array) - counter):
            if input_array[i] >> input_array[i + 1]:
                input_array[i], input_array[i + 1] = input_array[i + 1], input_array[i]
            
        counter += 1
            
    print(input_array)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
