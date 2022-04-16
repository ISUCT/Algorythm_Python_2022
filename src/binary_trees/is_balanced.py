'''
>>> import io, sys
>>> sys.stdin = io.StringIO('7 3 2 1 9 5 4 6 8 0')
>>> print_balanced()
YES
'''

from binary_tree_thing import *

def tree_depth(tree):
    if tree is None:
        return 0
    return max(tree_depth(tree.left), tree_depth(tree.right)) + 1

def tree_balanced(tree):
    if not tree or (((tree_depth(tree.left) == tree_depth(tree.right)) or (tree_depth(tree.left) + 1 == tree_depth(tree.right)) or tree_depth(tree.left) == tree_depth(tree.right) + 1) and tree_balanced(tree.right) and tree_balanced(tree.left)):
        return True
    return False

def print_balanced():
    print('YES' if tree_balanced(create_tree(list(map(int, input().split())))) else 'NO')

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)