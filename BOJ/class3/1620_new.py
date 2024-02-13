import sys
input = sys.stdin.readline
n, m = map(int, input().split())
poketmon = dict()
for i in range(n):
    name = input().rstrip()
    poketmon[str(i+1)] = name
    poketmon[name] = str(i+1)
for _ in range(m):
    order = input().rstrip()
    #reverse = {v:k for k, v in poketmon.items()}
    print(poketmon[order])