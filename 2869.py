import sys
import math
a, b, v = map(int, sys.stdin.readline().split())
k = (v-a)/(a-b)
print(math.ceil(k) + 1)
