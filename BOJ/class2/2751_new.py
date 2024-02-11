n = int(input())
numList = []
for i in range(n):
    numList.append(int(input()))
numList = sorted(numList)
for i in numList:
    print(i)