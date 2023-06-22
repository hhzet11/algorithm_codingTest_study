import sys
from itertools import permutations
input = sys.stdin.readline

# 1. 1~9까지의 모든 수 중에서 3개를 뽑아 조합한 순열 리스트를 만든다.
# 2. 민혁이가 질문한 숫자와 비교해 strike, ball의 개수를 따짐
# 3. 영수가 대답한 strike와 ball의 개수를 비교해 맞지 않을경우 리스트에서 제
n = int(input())
combi = list(permutations(range(1, 10), 3))
for _ in range(n):
    num, s, b = map(int, input().split())
    num = list(str(num))
    cnt = 0
    for i in range(len(combi)):
        strike, ball = 0, 0
        i -= cnt
        for j in range(3):
            num[j] = int(num[j])
            if num[j] in combi[i]:
                if j == combi[i].index(num[j]):
                    strike += 1
                else :
                    ball += 1
        if strike != s or ball != b:
            combi.remove(combi[i])
            cnt += 1
print(len(combi))
