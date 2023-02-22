n = int(input())
d = [[0 for i in range(10)] for i in range(1001)]
result = [0 for i in range(1001)]
result[1] = 10
for i in range(1, 10):
    d[1][i] = 1
for i in range(2, n+1):
    for j in range(1, 10):
        if j == 1:
            d[i][1] = d[i-1][1]
        else :
            d[i][j] = sum(d[i-1][1:j+1]) # d[i][j] = d[i-1][j] + d[i][j-1]
    result[i] = sum(d[i]) + result[i-1]
print(result[n] % 10007)