# 1차 풀이 - 성공
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
cnt = 0
chicken, home = [], []

for _ in range(n) :
    a = list(map(int, input().split()))
    cnt += a.count(2)
    arr.append(a)

def findChk():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                chicken.append((i, j))

def findHome():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                home.append((i, j))

def distance():
    whole = int(1e9)
    for comb in list(combinations(chicken, m)):
        city = 0
        for h in home :
            dist = int(1e9)
            for c in comb:
                dist = min(dist, abs(h[0] - c[0]) + abs(h[1] - c[1]))
            city += dist
        whole = min(city, whole)
    print(whole)

findChk()
findHome()
distance()

# 다른 사람 풀이
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))
result = 999999
house = []      # 집의 좌표
chick = []      # 치킨집의 좌표

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chick.append([i, j])

for chi in combinations(chick, m):  # m개의 치킨집 선택
    temp = 0            # 도시의 치킨 거리
    for h in house:
        chi_len = 999   # 각 집마다 치킨 거리
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)

print(result)