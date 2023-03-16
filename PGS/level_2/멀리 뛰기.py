import math
def solution(n):
    # 1차 풀이 - 실패
    answer = 0
    cnt2, cnt1 = n//2, n%2
    for i in range(cnt2+1) :
        arr = [2] *i +[1]*(cnt1 + 2*(cnt2-i))
        answer += int(math.factorial(len(arr)) / (math.factorial(arr.count(1)) * math.factorial(arr.count(2))))
    return answer % 1234567

    # 2차 풀이 - 성공
    arr = [0, 1, 2]
    for i in range(3, n + 1):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr[n] % 1234567

    # 다른 사람 풀이
    def solution(n):
        if n < 3:
            return n
        d = [0] * (n + 1)
        d[1] = 1
        d[2] = 2
        for i in range(3, n + 1):
            d[i] = d[i - 1] + d[i - 2]
        return d[n] % 1234567