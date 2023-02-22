string = input().split('-')
arr = []
for i in string :
    cnt = 0
    s = i.split('+')
    for j in s :
        cnt += int(j)
    arr.append(cnt)
count = arr[0]
for i in range(1, len(arr)) :
    count -= arr[i]
print(count)