'''
>>> import io, sys
>>> sys.stdin = io.StringIO('7 3 2 1 9 5 4 6 8 0')
>>> print_with_single()
2
9
'''

from binary_tree_thing import *

def print_with_single():
    create_tree(list(map(int, input().split()))).find_with_single()

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)