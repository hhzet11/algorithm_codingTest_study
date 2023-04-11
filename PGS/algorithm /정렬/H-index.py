def solution(citations):
    # 1차 풀이 - 실패 1
    h, cnt = 0, 1
    while h != len(citations)+1 :
        cnt = 0
        for i in citations :
            if i >= h :
                cnt += 1
        if h == cnt :
            return h
            break
        h+= 1
    return 0

# 다른 사람 풀이
def solution(citations):
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if i >= c:
            return i
    return len(citations)