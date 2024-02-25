n = int(input())
stair = []
for _ in range(n):
    stair.append(int(input()))

dp = [0] * n
if n <= 2:
    print(sum(stair))
else:
    dp[0] = stair[0]
    dp[1] = stair[1] + stair[0]
    for i in range(2, n):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])
    print(dp[n-1])