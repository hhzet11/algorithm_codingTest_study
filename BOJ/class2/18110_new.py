def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

arr = []
n = int(input())

if n == 0 :
    print(0)
else:
    for _ in range(n):
        arr.append(int(input()))
    arr.sort()
    nn = round2(n * 0.15)
    print(round2(sum(arr[nn:-nn] if nn else arr) / (n - 2 * nn)))