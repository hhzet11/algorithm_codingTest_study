def solution(number, limit, power):
    # 1차 풀이 - 시간 초과
    answer = 0
    num = [1] * number
    print(num)
    for i in range(2, number+1) :
        cnt = 1
        for j in range(2, i) :
            if i % j == 0 :
                cnt += 1
        num[i-1] += cnt
    for i in range(len(num)) :
        if num[i] > limit :
            num[i] = power
    return sum(num)

    # 2차 풀이 - 성공
    def solution(number, limit, power):
        answer = 0
        num = [0] * number
        for i in range(1, number + 1):
            data = set()
            for j in range(1, int(i ** 0.5) + 1):
                if i % j == 0:
                    data.add(j)
                    data.add(i // j)
            num[i - 1] += len(data)
        for i in range(len(num)):
            if num[i] > limit:
                num[i] = power
        return sum(num)