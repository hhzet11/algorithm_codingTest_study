test = int(input())
for _ in range(test):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_ = [0 for i in range(n)]
    arr_[m] = 1
    cnt = 0

    while True :
        if arr[0] == max(arr) :
            cnt += 1
            if arr_[0] == 1 :
                print(cnt)
                break
            else :
                del arr[0]
                del arr_[0]
        else :
            arr.append(arr[0])
            del arr[0]
            arr_.append(arr_[0])
            del arr_[0]

