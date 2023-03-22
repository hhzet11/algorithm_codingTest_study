def solution(n, a, b):
    # 1차시도 - 실패
    answer = 0
    num = n
    while num > 1:
        num /= 2
        answer += 1

    mid = n / 2
    while mid > 0:
        if a <= mid and b > mid:
            return answer
            break
        elif a > mid:
            a -= mid
            b -= mid
        mid = mid / 2
        answer -= 1


def solution(n, a, b):
    #2차 풀이 - 성공
    num = 2
    answer = 1
    while num <= n:
        if (a - 1) // num == (b - 1) // num:
            return answer
        else:
            num *= 2
            answer += 1

# 다른 사람 풀이
def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer
