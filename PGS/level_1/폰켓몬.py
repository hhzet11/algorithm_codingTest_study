from itertools import combinations as cb


def solution(nums):
    answer = 0
    '''
    # 1차 풀이 - 시간 초과 실패: for문을 통해 불필요한 과정 거침
    result = []
    for numb in cb(nums, int(len(nums)/2)) :
        result.append(len(set(numb)))
    answer = max(result)
    '''

    # 2차 풀이 - 성공
    unique_type = len(set(nums))
    if unique_type < len(nums) / 2:
        answer = unique_type
    else:
        answer = len(nums) / 2

    # best 풀이
    # min(len(nums)/2, len(set(nums)))

    return answer