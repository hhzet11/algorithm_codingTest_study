while True :
    arr = list(map(int, input().split()))
    max_ = max(arr)
    if sum(arr) == 0:
        break
    arr.remove(max_)
    if arr[0]**2 + arr[1]**2 == max_**2 :
        print("right")
    else :
        print("wrong")
