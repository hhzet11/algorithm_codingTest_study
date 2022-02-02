L = int(input())
container = input()
result, temp = 0, 0
for i in range(L) :
    result += (ord(container[i])-96) * (31 ** i)
print(result % 1234567891)
