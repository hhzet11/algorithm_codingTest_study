import math
n = int(input())
fact = list(str(math.factorial(n)))
temp = fact[-1]
count = 0
while fact[-1] == '0' :
    count += 1
    del fact[-1]
print(count)