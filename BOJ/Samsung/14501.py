# DP : 큰 문제를 작은 문제로 나누고, 반복되는 것을 이용해서 해결
# 부분 문제를 푸는 순서에 따라 Top-Down, Bottom-Up으로 나뉨

# Bottom-Up
# n = int(input())
# schedule = [list(map(int, input().split())) for i in range(n)]
# dp = [0 for i in range(n+1)]
#
# for i in range(n):
#     for j in range(i+schedule[i][0], n+1):
#         print(i, j)
#         if dp[j] < dp[i] + schedule[i][1]:
#             dp[j] = dp[i] + schedule[i][1]
#         print(dp)
# print(dp[-1])

# Top-Down
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    # i일에 상담을 하는 것이 퇴사일을 넘기면 상담 하지 않음
    if i + li[i][0] > n :
        dp[i] = dp[i+1]
    else:
        # i일에 상담하는 것과 아닌 것 중 최대 선택
        dp[i] = max(dp[i+1], li[i][1] + dp[i + li[i][0]])
print(dp[0])
