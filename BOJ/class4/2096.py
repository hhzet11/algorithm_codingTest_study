# 메모리 초과
import copy
n = int(input())
df = []
for i in range(n):
    df.append(list(map(int, input().split())))
df2 = copy.deepcopy(df)

#최대
for i in range(1, n) :
    for j in range(3):
        if j == 0 :
            df[i][j] += max(df[i-1][j], df[i-1][j+1])
        elif j == 1 :
            df[i][j] += max(df[i-1][j-1], df[i-1][j], df[i-1][j+1])
        else :
            df[i][j] += max(df[i-1][j-1], df[i-1][j])
maxVal = max(df[n-1])

# 최소
for i in range(1, n) :
    for j in range(3):
        if j == 0 :
            df2[i][j] += min(df2[i-1][j], df2[i-1][j+1])
        elif j == 1 :
            df2[i][j] += min(df2[i-1][j-1], df2[i-1][j], df2[i-1][j+1])
        else :
            df2[i][j] += min(df2[i-1][j-1], df2[i-1][j])
minVal = min(df2[n-1])
print(maxVal, minVal)

# 다른 사람 풀이
import sys
input = sys.stdin.readline

n = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

max_tmp = [0] * 3
min_tmp = [0] * 3

for i in range(n):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            max_tmp[j] = a + max(max_dp[j], max_dp[j + 1])
            min_tmp[j] = a + min(min_dp[j], min_dp[j + 1])
        elif j == 1:
            max_tmp[j] = b + max(max_dp[j - 1], max_dp[j], max_dp[j + 1])
            min_tmp[j] = b + min(min_dp[j - 1], min_dp[j], min_dp[j + 1])
        else:
            max_tmp[j] = c + max(max_dp[j], max_dp[j - 1])
            min_tmp[j] = c + min(min_dp[j], min_dp[j - 1])

    for j in range(3):
        max_dp[j] = max_tmp[j]
        min_dp[j] = min_tmp[j]

print(max(max_dp), min(min_dp))