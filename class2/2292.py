n = int(input())
num = 1
cnt = 1
while n > num :
    num += 6 * cnt
    cnt += 1
print(cnt)

'''
if n > 3 :
    n = (n-2) // 6
    arr = []
    arr.append(1)
    for i in range(1, n+1):
        arr.append(arr[i-1] + i + 1)

    for i in range(len(arr)):
        if n < arr[i] :
            print(i + 2)
            break

elif n > 1 :
    print(2)
else :
    print(1)
'''