def solution(places):
    answer = []
    tmp = 0
    for place in places:
        tmp += 1
        position = []
        for i in range(0, 5):
            for j in range(0, 5):
                if place[i][j] == 'P':
                    position.append([i, j])

        for i in range(0, len(position)):
            if tmp == len(answer):
                break
            for j in range(i + 1, len(position)):
                r1, r2 = position[i][0], position[j][0]
                c1, c2 = position[i][1], position[j][1]
                cnt = abs(r2 - r1) + abs(c2 - c1)
                if cnt == 1:
                    answer.append(0)
                    break
                elif cnt == 2:
                    print(r1, c1, r2, c2)
                    if r1 == r2 and place[r1][c1 + 1] == 'O':
                        print('1st', i, j, cnt)
                        answer.append(0)
                        break

                    elif c1 == c2 and place[r1 + 1][c1] == 'O':
                        print('2nd', i, j)
                        answer.append(0)
                        break

                    # 1차 풀이 - 실패
                    #elif (r1 == r2 + 1 or c1 == c2 + 1) and (place[r1][c2] == 'O' or place[r2][c1] == 'O'):
                    # 2차 풀이 - 성공
                    else:
                        if place[r1][c2] == 'O' or place[r2][c1] == 'O' :
                            print('3rd', i, j, cnt)
                            answer.append(0)
                            break
        if tmp != len(answer):
            answer.append(1)
    return answer

# 다른 사람 풀이
from collections import deque
def bfs(p):
    start = []

    for i in range(5):  # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])

    for s in start:
        queue = deque([s])  # 큐에 초기값
        visited = [[0] * 5 for i in range(5)]  # 방문 처리 리스트
        distance = [[0] * 5 for i in range(5)]  # 경로 길이 리스트
        visited[s[0]][s[1]] = 1

        while queue:
            y, x = queue.popleft()

            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:

                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1

                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []

    for i in places:
        answer.append(bfs(i))

    return answer