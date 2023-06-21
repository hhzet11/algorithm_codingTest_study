# 1차 풀이 : 실패 - 메모리 초과
# import sys
# from itertools import combinations
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# friend = [[] for _ in range(n+1)]
# for i in range(m):
#     f1, f2 = map(int, input().split())
#     friend[f1].append(f2)
#     friend[f2].append(f1)
#
# combi = list(combinations(range(1,n+1), 3))
# newCombi = []
# for c in combi :
#     if c[1] in friend[c[0]] and c[2] in friend[c[0]] and c[2] in friend[c[1]]:
#         newCombi.append(c)
#
# result = 4001
# for new in newCombi:
#     cnt = 0
#     for i in range(3):
#         for f in friend[new[i]]:
#             if f not in new :
#                 cnt += 1
#     result = min(result, cnt)
# if result == 4001 :
#     print(-1)
# else:
#     print(result)

# 다른 사람 풀이
# 입력된 친구가 모두 a, b, c의 친구인 경우, 3 친구의 친구 수 합의 최대는 m-6이다
# a를 정하고, b는 a의 친구 중 한명이고, C는 b의 친구면서, a의 친구인 경우에서 친구 수의 최소값을 찾는다.
# b>a, c>b 조건을 통해 먼저 순회한 조합을 순회하지 않도록 함
n, m = map(int, input().split())
relations = [list(map(int, input().split())) for _ in range(m)]
friends = [set() for _ in range(n+1)]
for r in relations :
    friends[r[0]].add(r[1])
    friends[r[1]].add(r[0])

num_friends = m
for a in range(n):
    for b in friends[a] :
        for c in friends[b]:
            if c in friends[a] :
                num_friends = min(num_friends, len(friends[a]) + len(friends[b]) + len(friends[c])-6)
if num_friends < m :
    print(num_friends)
else :
    print(-1)
