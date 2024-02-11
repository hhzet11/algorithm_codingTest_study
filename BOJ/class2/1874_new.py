import sys
n = int(sys.stdin.readline())
stack = []
numList = []
result = []
for i in range(n):
    numList.append(int(sys.stdin.readline()))
val = 0
for i in range(1, n+1):
    result.append('+')
    stack.append(i)

    while len(stack) > 0 and stack[-1] == numList[val]:
        result.append('-')
        stack.pop()
        val += 1
        if val == len(numList):
            break

    i += 1

if len(stack) > 0 :
    print('NO')
else :
    for i in result :
        print(i)


n = int(sys.stdin.readline())
temp = 0
stack = []
result = []
count = 1

for i in range(n):
    num = int(input())

    #입력받은 숫자까지 push
    while count <= num :
        stack.append(count)
        result.append('+')
        count += 1

    #num이랑 stack 맨 위 숫자가 동일하다면 pop
    if num == stack[-1]:
        stack.pop()
        result.append('-')
    else :
        temp = 1
        print('NO')
        break

if temp == 0:
    for i in result:
        print(i)

