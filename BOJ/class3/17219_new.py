import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pw = dict()
for _ in range(n):
    add = input().split()
    pw[add[0]] = add[1]
for _ in range(m):
    ask = input().rstrip()
    print(pw[ask])