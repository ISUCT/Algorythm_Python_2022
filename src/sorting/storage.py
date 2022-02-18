"""
>>> import io, sys
>>> sys.stdin = io.StringIO(chr(10).join([\
'5',\
'1 50 3 4 3',\
'16',\
'1 2 3 4 5 1 3 3 4 5 5 5 5 5 4 5'\
]))
>>> storage()
yes
no
no
no
yes
"""

def sorting(orders):
    sorted = [0] * max(orders)
    for item in orders:
        sorted[item-1] += 1
    return sorted

def storage():
    product_types = int(input())
    products = list(map(int,input().split(" ")))
    orders_count = int(input())
    orders = list(map(int,input().split(" ")))
    sorted = sorting(orders)
    for i in range(len(products)):
        if products[i] >= sorted[i]:
            print("no")
        else:
            print("yes")

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
