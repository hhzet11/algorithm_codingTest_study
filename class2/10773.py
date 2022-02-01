k = int(input())
arr = []
for _ in range(k):
    num = int(input())
    if num != 0:
        arr.append(num)
    else :
        arr.pop()
if len(arr) != 0:
    print(sum(arr))
else : print(0)
