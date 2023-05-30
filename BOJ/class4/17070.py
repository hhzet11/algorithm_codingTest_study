import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1 #시작위치

#dp를 위해서는 윗행을 사용해야하므로, 첫행 초기화
for i in range(2, n):
    if arr[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

for r in range(1, n):
    for c in range(1, n):
        # 대각선이면
        if arr[r][c] == 0 and arr[r][c-1] == 0 and arr[r-1][c] == 0:
            dp[2][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]
        if arr[r][c] == 0 :
            # 가로면
            dp[0][r][c] = dp[0][r][c-1] + dp[2][r][c-1]
            # 세로면
            dp[1][r][c] = dp[1][r-1][c] + dp[2][r-1][c]

print(sum(dp[i][n-1][n-1] for i in range(3)))