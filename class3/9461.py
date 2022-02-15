import sys
T = int(sys.stdin.readline())
for _ in range(T) :
    n = int(sys.stdin.readline())
    arr = [1, 1, 1, 2, 2]
    for i in range(5, n):
        arr.append(arr[-1] + arr[i-5])
    print(arr[n-1])