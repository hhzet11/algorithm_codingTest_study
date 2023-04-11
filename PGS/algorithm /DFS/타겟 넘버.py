from itertools import product
def solution(numbers, target):
    # 1차 풀이 - 성공
    answer = 0
    #다른 사람 풀이
    # num_list = [(n, -n) for n in numbers]
    num_list = []
    for n in numbers :
        num_list.append((n, -n))

    product_list = list(product(*num_list))
    for p in product_list :
        if sum(p) == target :
            answer += 1
    return answer

# 다른 사람 풀이
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

# 다른 사람 풀이 - dfs
answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer