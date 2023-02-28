def solution(d, budget):
    # 1차 풀이 - 실패
    def solution(d, budget):
        d.sort()
        for i in range(1, len(d)):
            d[i] = d[i - 1] + d[i]
            if d[i] > budget:
                return i
            elif d[i] == budget:
                return i + 1

    # 다른 사람 풀이
    d.sort()
    while budget < sum(d) :
        d.pop()
    return len(d)