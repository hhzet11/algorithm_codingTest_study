#2차시도 - 성공
def solution(m, n, board):
    answer = 0
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    value = []
    for i in board :
        value.append(list(i))
    keep = True
    while keep:
        del_list = []
        # 2*2 발견하기
        for i in range(m) :
            for j in range(n) :
                cnt = 0
                for k in range(3):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0<=nx<m and 0<=ny<n and value[i][j] == value[nx][ny] and value[i][j] != 0 :
                        cnt += 1
                if cnt == 3:
                    del_list.append([i, j])
                    for k in range(3):
                        nx, ny = i + dx[k], j + dy[k]
                        del_list.append([nx, ny])
        if len(del_list) == 0 :
            keep = False
        #지우기
        for d in del_list :
            value[d[0]][d[1]] = 0
        for i in range(m) :
            for j in range(n) :
                if value[i][j] == 0 :
                    # 밑에서부터 끌어올리기 - 2차 수정
                    for k in range(i, 0, -1):
                        value[k][j], value[k-1][j] = value[k-1][j], value[k][j]
    for i in value :
        answer += i.count(0)
    return answer