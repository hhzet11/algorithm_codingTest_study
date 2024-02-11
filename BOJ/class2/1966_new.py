from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    r = 0
    while queue:
        best = max(queue)
        front = queue.popleft()
        m -= 1

        if front == best:
            r += 1
            if m < 0:
                print(r)
                break

        else :
            queue.append(front)
            if m < 0 :
                m = len(queue)-1