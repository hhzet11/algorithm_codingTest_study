import string
import math


def convert(n, k):
    tmp = string.digits + string.ascii_lowercase
    q, r = divmod(n, k)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, k) + tmp[r]

def isprime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# 1차 풀이 - 성공
def solution(n, k):
    num = str(convert(n, k))
    prime = list(num.split('0'))
    answer = 0
    for p in prime:
        if p == '' or p == '1':
            continue
        if isprime(int(p)):
            answer += 1
    return answer