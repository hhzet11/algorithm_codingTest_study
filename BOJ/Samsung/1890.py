n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == j == n-1:
            print(dp[i][j])
            break
        cursor = graph[i][j]

        if i + cursor < n :
            dp[i+cursor][j] += dp[i][j]
        if j + cursor < n :
            dp[i][j+cursor] += dp[i][j]
