import sys
import math
input = sys.stdin.readline

m = int(input())
X = 1000000007
expect = 0

def getExpectedValue(n, s):
    return s * getSquaredNumber(n, X-2) % X

def getSquaredNumber(num, exp):
    if exp == 1 :
        return num
    if exp % 2 == 0:
        half = getSquaredNumber(num, exp//2)
        return half * half % X
    else:
        return num*getSquaredNumber(num, exp-1) % X

for _ in range(m):
    i, s = map(int, input().split())
    gcd = math.gcd(i, s)
    i //= gcd
    s //= gcd
    expect += getExpectedValue(i, s)
    expect %= X
print(expect)