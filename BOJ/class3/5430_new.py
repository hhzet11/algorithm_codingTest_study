from collections import deque

T = int(input())
while T > 0 :
    T -= 1
    p = list(input().strip())
    n = int(input())

    num = input().strip()
    numList = deque(num[1:-1].split(','))
    if n == 0:
        numList = deque()

    count = 0
    flag = 0
    for i in p:
        if i == 'R':
            count += 1
        else:
            if len(numList) == 0:
                print('error')
                flag = 1
                break
            else:
                if count %2 == 0:
                    numList.popleft()
                else :
                    numList.pop()
    if flag == 0:
        if count %2 == 0 :
            print('[' + ",".join(numList) + ']')
        else:
            numList.reverse()
            print('[' + ",".join(numList) + ']')