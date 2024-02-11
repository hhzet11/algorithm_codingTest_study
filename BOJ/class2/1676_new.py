n = int(input())
fact = 1
for i in range(2, n+1):
    fact *= i

result = 0
fact = str(fact)[::-1]
print(len(fact) - len(str(int(fact))))