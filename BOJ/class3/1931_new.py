n = int(input())
table = []
for _ in range(n):
    start, end = map(int, input().split())
    table.append([start, end])
table.sort(key = lambda x: (x[1], x[0]))

cnt = 0
endPoint = 0
for start, end in table:
    if endPoint <= start :
        cnt += 1
        endPoint = end
print(cnt)

