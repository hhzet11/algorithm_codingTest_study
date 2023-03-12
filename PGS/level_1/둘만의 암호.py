import string
def solution(s, skip, index):
    # 1차 풀이 - 실패 : 런타임 에러
    answer = ''
    alpha = list(string.ascii_lowercase)
    for i in skip :
        alpha.remove(i)
    for i in s :
        idx = alpha.index(i)
        '''
        if idx + index < len(alpha) :
            answer += alpha[idx+index]
        else :
            answer += alpha[idx+index - len(alpha)]
        '''
        # 2차 풀이 - 성공
        answer += alpha[(idx+index) % len(alpha)]
    return answer