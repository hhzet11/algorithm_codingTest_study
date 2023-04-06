# 1차 풀이 - 실패
def solution(k, tangerine):
    answer = 0
    count = {}
    for i in tangerine:
        if i not in count:
            # 시간 초과
            #count[i] = tangerine.count(i)
            count[i] = 1
        else :
            count[i] += 1
    count = sorted(count.values(), reverse=True)
    '''
    for i in count:
        if k < i:
            continue
        else:
            if k - i < 0:
                continue
            elif k - i == 0:
                k -= i
                answer += 1
                break
            else:
                k -= i
                answer += 1
    '''
    # 2차 풀이 - 성공
    for i in count:
        if k <= 0:
            return answer
        k -= i
        answer += 1
    return answer