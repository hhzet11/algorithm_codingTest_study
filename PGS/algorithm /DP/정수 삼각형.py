# 1차 풀이 - 성공
def solution(triangle):
    for i, tri in enumerate(triangle) :
        for j in range(len(tri)) :
            if i > 0 :
                if j == 0 :
                    triangle[i][0] += triangle[i-1][0]
                elif j == len(tri) - 1 :
                    triangle[i][j] += triangle[i-1][j-1]
                else :
                    triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    return max(triangle[-1])