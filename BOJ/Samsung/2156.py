n = int(input())
drink = [int(input()) for _ in range(n)]
dp = [0] * n

dp[0] = drink[0]
if n > 1:
    dp[1] = drink[0] + drink[1]
if n > 2:
    dp[2] = max(dp[1], drink[0]+drink[2], drink[1]+drink[2])
for i in range(3, n):
    dp[i] = max(dp[i-2]+drink[i], dp[i-3]+drink[i-1]+drink[i], dp[i-1])
print(dp[-1])