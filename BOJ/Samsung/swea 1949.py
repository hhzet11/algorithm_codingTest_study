def dfs(row, col, k, check, cnt):  # 행,열, 굴삭깊이, 굴삭했는지 체크 parameter, 등산로길이
    global max_cnt
    for i in range(4):  # 4방향 체크
        if 0 <= row + dx[i] < N and 0 <= col + dy[i] < N and mapp[row][col] > mapp[row + dx[i]][col + dy[i]] and not \
        visit[row + dx[i]][col + dy[i]]:  # 맵 범위 벗어나는지, 다음칸이 지금보다 작은지, 방문하지 않았는지
            new_cnt = cnt + 1  # 등산로 길이를 늘려주고
            visit[row + dx[i]][col + dy[i]] = 1  # 다음칸 방문했음을 알림
            dfs(row + dx[i], col + dy[i], k, check, new_cnt)  # 다시 dfs 탐색
            visit[row + dx[i]][col + dy[i]] = 0  # 백트래킹 후 방문배열 해제
        elif 0 <= row + dx[i] < N and 0 <= col + dy[i] < N and mapp[row][col] <= mapp[row + dx[i]][
            col + dy[i]] and check == 0 and not visit[row + dx[i]][
            col + dy[i]]:  # 맵 범위 벗어나는지, 다음칸이 같거나 크다면 굴삭할껀데 이미 굴삭한 적 없고 방문하지 않아야함.
            for j in range(1, k + 1):  # 굴삭깊이 1~k만큼 파봄
                mapp[row + dx[i]][col + dy[i]] -= j  # 판 깊이 만큼 높이 깎아줌
                if mapp[row][col] > mapp[row + dx[i]][col + dy[i]]:  # 깎은 높이가 낮아져서 등산로로 활용할 수 있다면
                    visit[row + dx[i]][col + dy[i]] = 1  # 방문할꺼기에 방문배열 체크
                    new_cnt = cnt + 1  # 등산로 길이 1 올려주고
                    dfs(row + dx[i], col + dy[i], k - j, 1, new_cnt)  # 다시 다음 등산로를 탐색
                    visit[row + dx[i]][col + dy[i]] = 0  # 백트래킹 후 방문 배열 해제
                mapp[row + dx[i]][col + dy[i]] += j  # 백트래킹 했으므로 깎은 산 높이도 정상화 시킴
    if max_cnt < cnt:  # 4방향체크를 다하고 갈 곳이 없으면 max값과 비교 후 return
        max_cnt = cnt
    return


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    mapp = [list(map(int, input().split())) for _ in range(N)]

    max_arr = []  ## 최고 높이를 구하는 과정
    for i in range(N):
        max_arr.append(max(mapp[i]))
    maxx = max(max_arr)

    max_cnt = -9999999

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visit = [[0 for _ in range(N)] for _ in range(N)]  # 방문배열
    for y in range(N):
        for x in range(N):
            if mapp[x][y] != maxx:  # 최고 봉우리가 아니면 pass시킴
                continue
            visit[x][y] = 1  # 너무 중요하다... 첫 시작지점도 방문했음에 체크를 해줘야한다.
            dfs(x, y, K, 0, 1)
            visit[x][y] = 0
    print('#{} {}'.format(t + 1, max_cnt))
