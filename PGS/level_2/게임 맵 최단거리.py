from collections import deque
# 다른 사람 풀이
def solution(maps):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        # queue가 빌 때까지 반복
        while queue:
            x, y = queue.popleft()
            # 상하좌우 칸 확인하기
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 처음 지나가는 길이면 거리계산하고 다시 상하좌우 확인하기
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))  # 재귀

        # 상대 팀 진영(제일 오른쪽 아래 칸)까지의 거리 반환
        return maps[-1][-1]

    answer = bfs(0, 0)
    return -1 if answer == 1 else answer