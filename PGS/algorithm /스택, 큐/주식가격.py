# 1차 풀이 - 실패 : 효율성 테스트 시간초과
def solution(prices):
    answer = []
    for i, price in enumerate(prices[:-1]) :
        down = False
        for j, p in enumerate(prices[i+1:]) :
            if price > p :
                down = True
                answer.append(j+1)
                break
        if not down :
            answer.append(len(prices) - i - 1)
    answer.append(0)
    return answer

# 다른 사람 풀이
from collections import deque
def solution(prices):
    queue = deque(prices)
    answer = []
    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break
        answer.append(sec)
    return answer