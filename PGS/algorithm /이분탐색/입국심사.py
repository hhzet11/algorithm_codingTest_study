# 1차 풀이 - 실패 : 시간초과
def solution(n, times):
    num = []
    for t in times :
        for i in range(1, n+1) :
            num.append(t * i)
    num.sort()
    return num[n-1]

# 다른 사람 풀이
def solution(n, times):
    l, r = 1, max(times) * n
    while l <= r:
        mid = (l + r) // 2
        people = 0
        for t in times:
            people += mid // t
            if people >= n:
                break
        if people >= n:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1
    return answer
