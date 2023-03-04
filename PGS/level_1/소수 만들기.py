from itertools import combinations
def solution(nums):
    # 1차 풀이 - 성공
    numList = list(combinations(nums, 3))
    answer = len(numList)
    for i in numList :
        tmp = int(sum(i))
        for j in range(2, int(tmp ** 0.5) + 1):
            if tmp % j == 0 :
                answer -= 1
                break
    return answer