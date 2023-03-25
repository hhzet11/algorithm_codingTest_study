# 1차풀이 - 성공
import math
def solution(arr):
    for i in range(len(arr)-1, 0, -1) :
        num = int(arr[i] * arr[i-1] / math.gcd(arr[i], arr[i-1]))
        arr.pop()
        arr.pop()
        arr.append(num)
    return arr[-1]

# 다른 사람 풀이
import math
def solution(arr):
    answer = arr[0]
    for n in arr:
        answer = n * answer // math.gcd(n, answer)
    return answer
