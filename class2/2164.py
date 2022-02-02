from collections import deque
n = int(input())
deque = deque([i for i in range(1, n+1)])
while len(deque) > 1 :
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)
print(deque[0])

'''
n = int(input())
arr = [i for i in range(1, n+1)] # list(range(1, n+1))
cnt = 1
while len(arr) > 1 :
    if cnt % 2 != 0 :
        del arr[0]
    else :
        temp = arr[0]
        del arr[0]
        arr.append(temp)
    cnt += 1
print(arr[0])
'''
