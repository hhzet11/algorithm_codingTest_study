import sys
input = sys.stdin.readline

# 벨만포드 응용 -> 그래프상 음의 싸이클 존재 판단 함수
def bf(start):
    dist = [int(1e9)] * (n + 1)
    dist[start] = 0
    for i in range(n) :
        for j in range(len(edges)) :
            cur, next, cost = edges[j]
            # 다음 노드로 이동하는 거리가 최단거리로 갱신 가능한 경우
            if dist[next] > dist[cur] + cost :
                dist[next] = dist[cur] + cost
                # n번 돌린건데 이때도 갱신이 발생하면 음의 싸이클이 존재함 이미
                if i == n-1 :
                    return True
    return False

TC = int(input())

for _ in range(TC) :
    n, m, w = map(int, input().split())
    edges = []

    for i in range(m+w) :
        s, e, t = map(int, input().split())
        if i >= m :
            t = -t # 웜홀
        else :
            edges.append((e, s, t)) # 반대 방향도 넣어줌
        edges.append((s, e, t)) # 원래 방향으로 웜홀 -t 반영 완료

    # 시작위치는 아무거나 무관
    # bf는 최단거리가 아닌, 음의 싸이클 유무 판단 알고리즘
    if bf(1) :
        print("YES")
    else :
        print("NO")