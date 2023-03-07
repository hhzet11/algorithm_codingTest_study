def solution(n, lost, reserve):
    # n차 풀이 - 성공
    def solution(n, lost, reserve):
        answer = n
        for i in range(1, n + 1):
            if i in lost and i in reserve:
                reserve.remove(i)
                lost.remove(i)

        for i in range(1, n + 1):
            if i in lost:
                if i - 1 in reserve:
                    reserve.remove(i - 1)
                elif i + 1 in reserve:
                    reserve.remove(i + 1)
                else:
                    answer -= 1
        return answer

    # 다른 사람 풀이

    # lost, reserve 서로 겹치지 않는 것들로만 구성!
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
