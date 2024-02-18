n = int(input())
p = list(map(int, input().split()))
p.sort()
res = 0
n = len(p)
for i in p:
    res +=  i * n
    n -= 1
print(res)
