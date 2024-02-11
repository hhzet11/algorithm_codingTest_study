n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

for num in b :
    l, r = 0, n-1
    exist = 0

    while l <= r :
        mid = (l + r) // 2
        if num == a[mid]:
            exist = 1 # 찾음
            print(1)
            break
        elif num > a[mid]:
            l = mid + 1
        else :
            r = mid - 1

    if exist == 0 :
        print(0)

