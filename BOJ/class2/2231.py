n = int(input())
res = False
for num in range(n):
    result = 0
    result += num
    arr = [int(i) for i in str(num)]
    result += sum(arr)
    if result == n:
        print(num)
        res = True
        break
if not res:
    print(0)