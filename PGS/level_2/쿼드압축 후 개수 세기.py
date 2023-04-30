# 다른 사람 풀이
def solution(arr):
    result = [0, 0]
    length = len(arr)

    def split(a, b, l):
        start = arr[a][b]
        for i in range(a, a + l):
            for j in range(b, b + l):
                if arr[i][j] != start:
                    l //= 2
                    split(a, b, l)
                    split(a, b + l, l)
                    split(a + l, b, l)
                    split(a + l, b + l, l)
                    return
        result[start] += 1

    split(0, 0, length)

    return result