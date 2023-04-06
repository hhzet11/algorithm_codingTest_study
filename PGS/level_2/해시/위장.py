from itertools import product, combination
def solution(clothes):
    cloth = {}
    for i, j in clothes:
        if j not in cloth:
            cloth[j] = 1
        else:
            cloth[j] += 1
    '''
    answer = sum(cloth.values())
    num, result = [], []
    for i in cloth.values():
        num.append(range(i))
    for i in range(2, len(num) + 1):
        result += list(combinations(num, i))
    for i in result:
        answer += len(list(product(*i)))
    return answer
    '''
    # 2차 풀이 - 성공
    answer = 1
    for i in cloth.values():
        answer *= (i + 1)
    return answer - 1