from collections import deque
def solution(priorities, location):
    # 1차 풀이 - 성공
    queue = deque()
    for i, p in enumerate(priorities):
        queue.append((i, p))
    max_q = max(queue, key=lambda x: x[1])

    answer = []
    while queue:
        x, y = queue.popleft()
        if y != max_q[1]:
            queue.append((x, y))
        else:
            answer.append(x)
            if len(queue) > 0:
                max_q = max(queue, key=lambda x: x[1])

    return answer.index(location) + 1

# 다른 사람 풀이
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer