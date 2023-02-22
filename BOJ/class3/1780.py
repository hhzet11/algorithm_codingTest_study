n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = [0,0,0]
def check(x, y, n):
    num = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != arr[i][j]:
                n = n//3
                for a in range(3):
                    for b in range(3):
                        check(x+n*a, y+n*b, n)
                return
    result[num] += 1

check(0, 0, n)
for i in range(-1, 2):
    print(result[i])