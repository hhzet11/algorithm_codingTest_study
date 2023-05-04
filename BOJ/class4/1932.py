n = int(input())
df = []
for i in range(n) :
    df.append(list(map(int, input().split())))
for i in range(1, n) :
    if i == 1 :
        df[i][0] += df[0][0]
        df[i][1] += df[0][0]
    else :
        for j in range(i+1):
            if j == 0 :
                df[i][j] += df[i-1][0]
            elif j == i :
                df[i][j] += df[i-1][j-1]
            else :
                df[i][j] += max(df[i-1][j], df[i-1][j-1])
print(max(df[n-1]))