import sys
num = int(sys.stdin.readline())
arr = []
for _ in range(num):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        arr.append(com[1])
    elif com[0] == 'front':
        if len(arr) != 0:
            print(arr[0])
        else : print(-1)
    elif com[0] == 'back':
        if len(arr) != 0:
            print(arr[-1])
        else : print(-1)
    elif com[0] == 'size':
        print(len(arr))
    elif com[0] == 'empty':
        if len(arr) != 0:
            print(0)
        else : print(1)
    elif com[0] == 'pop':
        if len(arr) != 0:
            temp = arr[0]
            arr.pop(0)
            print(temp)
        else :
            print(-1)
