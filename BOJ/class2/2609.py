from math import gcd
n, m = map(int, input().split())
cnt = gcd(n, m)
print(cnt)
print((n//cnt)*(m//cnt)*cnt)
