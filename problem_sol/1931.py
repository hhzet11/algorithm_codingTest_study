n = int(input())
time = []
for _ in range(n):
    start, end = map(int, input().split())
    time.append([start, end])

time = sorted(time, key=lambda a: (a[1], a[0]))
print(time)

