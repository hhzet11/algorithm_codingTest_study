import math
def solution(n, m):
    # 1차 풀이 - 성공
    # math 라이브러리 활용
    return [math.gcd(n, m), (n * m) // math.gcd(n,m)]

    # 2차 풀이
    for i in range(min(n,m), 0, -1):
        if n % i == 0 and m % i == 0:
            gcd = i
            break
    return [gcd, (n * m) // gcd]