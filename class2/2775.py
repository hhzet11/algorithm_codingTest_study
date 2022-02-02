T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    arr = [[0 for col in range(n)] for row in range(k+1)]
    for i in range(k+1):
        sum = 0
        for j in range(n):
            if i == 0 :
                arr[i][j] = j+1
            else :
                sum += arr[i-1][j]
                arr[i][j] = sum
    print(arr[k][n-1])
