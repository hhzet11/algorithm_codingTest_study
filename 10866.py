import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    com = sys.stdin.readline().split()
    if com[0] == 'push_front':
        arr.insert(0, com[1])
    elif com[0] == 'push_back':
        arr.append(com[1])
    elif com[0] == 'pop_front':
        if len(arr) != 0 :
            temp = arr[0]
            print(temp)
            arr.pop(0)
        else : print(-1)
    elif com[0] == 'pop_back':
        if len(arr) != 0 :
            temp = arr[-1]
            print(temp)
            arr.pop()
        else : print(-1)
    elif com[0] == 'size':
        print(len(arr))
    elif com[0] == 'empty':
        if len(arr) != 0:
            print(0)
        else : print(1)
    elif com[0] == 'front':
        if len(arr) != 0:
            print(arr[0])
        else : print(-1)
    elif com[0] == 'back':
        if len(arr) != 0:
            print(arr[-1])
        else : print(-1)