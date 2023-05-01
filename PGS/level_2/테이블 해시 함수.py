# 1차 풀이 - 성공
def solution(data, col, row_begin, row_end):
    answer = []
    data.sort(key=lambda x: [x[col - 1], -x[0]])
    for i in range(row_begin, row_end + 1):
        mod = 0
        for d in data[i - 1]:
            mod += d % i
        answer.append(mod)

    result = answer[0]
    if len(answer) == 1:
        return result
    else:
        for a in answer[1:]:
            result ^= a
        return result