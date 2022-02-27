"""
>>> import io, sys 
>>> sys.stdin = io.StringIO(chr(10).join(['9',\
'12',\
'32',\
'45',\
'67',\
'98',\
'29',\
'61',\
'35',\
'09',\
]))  
>>> radix()
Initial array:
12, 32, 45, 67, 98, 29, 61, 35, 09
**********
Phase 1
Bucket 0: empty
Bucket 1: 61
Bucket 2: 12, 32
Bucket 3: empty
Bucket 4: empty
Bucket 5: 45, 35
Bucket 6: empty
Bucket 7: 67
Bucket 8: 98
Bucket 9: 29, 09
**********
Phase 2
Bucket 0: 09
Bucket 1: 12
Bucket 2: 29
Bucket 3: 32, 35
Bucket 4: 45
Bucket 5: empty
Bucket 6: 61, 67
Bucket 7: empty
Bucket 8: empty
Bucket 9: 98
**********
Sorted array:
09, 12, 29, 32, 35, 45, 61, 67, 98
"""
def radix():
    n = int(input())
    strings = []
    for i in range(n):
        strings.append(input())
    rank = len(strings[0])
    print('Initial array:')
    print(', '.join(strings))
    phase = 1
    for i in range(rank - 1, -1, -1):
        print('**********')
        print('Phase', phase)
        buckets = [[] for _ in range(10)]
        for j in range(len(strings)):
            buckets[int(strings[j][i])].append(strings[j])
        for j in range(10):
            if len(buckets[j]) == 0:
                print('Bucket', str(j) + ': empty')
            else:
                print('Bucket', str(j) + ':', ', '.join(buckets[j]))
        pos = 0
        for j in range(10):
            for k in range(len(buckets[j])):
                strings[pos] = buckets[j][k]
                pos += 1
        phase += 1
    print('**********')
    print('Sorted array:')
    print(', '.join(strings))
    
if __name__ == '__main__':
    import doctest
doctest.testmod(verbose=True)