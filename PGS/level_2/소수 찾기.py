# 1차 풀이 - 성공
from itertools import permutations
import math
def isprime(x):
    for j in range(2, int(math.sqrt(x)+1)):
        if x % j == 0:
            return 0
    return 1

def solution(numbers):
    number = list(numbers)
    num_list, num = [], []
    answer = 0
    for i in range(1, len(number)+1):
        num_list += list(permutations(number, i))
    for i in num_list :
        n = ''
        for j in i :
            n += str(j)
        num.append(int(n))
    for i in set(num) :
        if i > 1:
            answer += isprime(i)
    return answer

# 다른 사람 풀이
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)