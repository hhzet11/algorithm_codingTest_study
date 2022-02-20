n = int(input())
arr = []
for i in range(n):
    arr.append(input())
result = []

def check(x, y, n) :
    num = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != arr[i][j]:
                result.append('(')
                check(x, y, n//2)
                check(x, y+n//2, n//2)
                check(x+n//2, y, n//2)
                check(x+n//2, y+n//2, n//2)
                result.append(')')
                return
    result.append(num)
check(0, 0, n)
for i in result:
    print(i, end='')