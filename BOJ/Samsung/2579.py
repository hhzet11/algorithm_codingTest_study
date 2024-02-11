n = int(input())
stair = [int(input()) for _ in range(n)]
dp = [0] * n # dp 리스트 생성

# 계단이 2개 이하일 때
if len(stair) <= 2 :
    print(sum(stair))
else :
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1] # 두번째까지는 수동 계산
    for i in range(2, n): # 점화식 통해서 계산
        #이전 3번째 칸에서 2번 뛰어넘어 바로 앞칸과의 값 / 이전 두번째칸에서 넘어온 것
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

    print(dp[-1])