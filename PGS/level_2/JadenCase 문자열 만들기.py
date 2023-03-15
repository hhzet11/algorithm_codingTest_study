def solution(s):
    answer = ''
    # 1차시도 - 실패
    s=list(map(str, s.split()))
    # 다른 사람 풀이
    s=s.split(' ')

    for i in range(len(s)):
        s[i]=s[i].capitalize()
    answer=' '.join(s)
    return answer