import sys
input = sys.stdin.readline
arr = set()
m = int(input())
for _ in range(m):
    order = input().split()
    if len(order) > 1:
        order[1] = int(order[1])

    if order[0] == 'add':
        arr.add(order[1])
    elif order[0] == 'remove' and order[1] in arr:
        arr.discard(order[1])
    elif order[0] == 'check':
        if order[1] in arr : print(1)
        else : print(0)
    elif order[0] == 'toggle':
        if order[1] in arr : arr.discard(order[1])
        else: arr.add(order[1])
    elif order[0] == 'all':
        arr = {i for i in range(1, 21)}
    elif order[0] == 'empty':
        arr = set()
