n = int(input())
arr = [0, 1, 3]
for i in range(3, 1001):
    arr.append(arr[i-1] + (arr[i-2]*2))
print(arr[n] % 10007)