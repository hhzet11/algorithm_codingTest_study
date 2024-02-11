T = int(input())
while T > 0:
    T -= 1
    x = input()
    arr = []

    for i in x :
        if i == '(':
            arr.append(i)
        else:
            if len(arr) > 0 and arr[-1] == '(':
                arr.pop()
            else:
                arr.append(i)
                break
    if len(arr) > 0:
        print('NO')
    else:
        print('YES')