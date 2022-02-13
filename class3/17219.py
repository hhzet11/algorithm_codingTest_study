n, m = map(int, input().split())
arr = {}
for i in range(n):
    site, pw = map(str, input().split())
    arr[site] = pw

for i in range(m):
    find = input()
    print(arr[find])
