# 1차 풀이 - 런타임 에러, 시간 초과
def fibo(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fibo(n-1) + fibo(n-2)

def solution(n):
    return fibo(n) % 1234567

# 2차 풀이 - 성공
def solution(n):
    f = [0] * (n+1)
    f[1] = 1
    for i in range(2, n+1) :
        f[i] = f[i-1] + f[i-2]
    return f[n] % 1234567