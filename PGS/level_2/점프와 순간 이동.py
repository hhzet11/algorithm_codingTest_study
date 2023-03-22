def solution(n):
    # 1차 시도 - 효율성 테스트 실패
    battery = [0] * (n+1)
    i=1
    while i <= n :
        if battery[i] == 0 and i %2 == 0:
            battery[i] = battery[i//2]
        elif battery[i] ==0 and i%2 != 0 :
            battery[i] = battery[i-1] +1
        i+=1

    return battery[n]

def solution(n):
    # 2차 시도 - 효율성 테스트 1개 실패 : 시간 초과
    answer = 1
    while n > 1 :
        if n %2 == 1 :
            answer += 1
        n //= 2

    return answer

# 3차 시도 - 해결
def solution(n):
    answer = 1
    while n > 1 :
        answer += n % 2
        n //= 2

    return answer
