import sys
T = int(sys.stdin.readline())
stack = []
for _ in range(T):
    command = sys.stdin.readline().split()
    if command[0] == 'push' :
        num = command[1]
        stack.append(num)
    elif command[0] == 'top' :
        if len(stack) != 0 :
            print(stack[-1])
        else :
            print(-1)
    elif command[0] == 'size' :
        print(len(stack))
    elif command[0] == 'empty' :
        if len(stack) != 0 :
            print(0)
        else :
            print(1)
    elif command[0] == 'pop' :
        if len(stack) != 0 :
            print(stack[-1])
            stack.pop()
        else :
            print(-1)
