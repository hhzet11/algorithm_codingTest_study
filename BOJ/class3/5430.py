import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
while T > 0 :
    T -= 1
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(",")
    queue = deque(arr)

    rev, front, back = 0, 0, len(queue)-1
    flag = 0
    if n == 0 :
        queue = []
        front = 0
        back = 0

    for i in p:
        if i == 'R' :
            rev += 1
        elif i == 'D' :
            if len(queue) < 1  :
                flag = 1
                print('error')
                break
            else :
                if rev % 2 == 0 :
                    queue.popleft()
                else :
                    queue.pop()

    if flag == 0:
        if rev % 2 == 0 :
            print("[" + ",".join(queue) + "]")
        else :
            queue.reverse()
            print("[" + ",".join(queue) + "]")