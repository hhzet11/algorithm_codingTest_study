import sys
n, k = map(int, sys.stdin.readline().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))

count = 0
for i in reversed(range(n)) :
    count += k // coin[i]
    k %= coin[i]
print(count)