# # 1차 풀이 - 실패
# n, m = map(int, input().split())
# true = list(input().split()[1:])
#
# party = []
# for _ in range(m) :
#     p = list(input().split()[1:])
#     party.append(p)
#
# for p in party :
#     for i in p :
#         if i in true and len(p) > 1 :
#             true += p
#
# true = list(set(true))
# answer = 0
# for p in party :
#     for i in p :
#         if i in true :
#             break
#         if i == p[-1]:
#             answer += 1
# print(answer)

# 다른 사람 풀이
n, m = map(int, input().split())
knowList = set(input().split()[1:])
parties = []

for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for party in parties:
        if party & knowList: #교집합 존재할 경우에
            knowList = knowList.union(party) # 합집합으로 만들기
    print(knowList)

cnt = 0
for party in parties:
    if party & knowList:# # 1차 풀이 - 실패
# n, m = map(int, input().split())
# true = list(input().split()[1:])
#
# party = []
# for _ in range(m) :
#     p = list(input().split()[1:])
#     party.append(p)
#
# for p in party :
#     for i in p :
#         if i in true and len(p) > 1 :
#             true += p
#
# true = list(set(true))
# answer = 0
# for p in party :
#     for i in p :
#         if i in true :
#             break
#         if i == p[-1]:
#             answer += 1
# print(answer)

# 다른 사람 풀이
n, m = map(int, input().split())
knowList = set(input().split()[1:])
parties = []

for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for party in parties:
        if party & knowList: #교집합 존재할 경우에
            knowList = knowList.union(party) # 합집합으로 만들기

cnt = 0
for party in parties:
    if party & knowList:
        continue
    cnt += 1

print(cnt)
        continue
    cnt += 1

print(cnt)