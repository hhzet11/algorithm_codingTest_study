T = int(input())
for _ in range(T):
    pthesis = list(input())
    arr = []
    temp = True
    for i in pthesis :
        if i == '(' :
            arr.append(i)
        elif i == ')' :
            if not arr :
                temp = False
                break
            elif arr[-1] == '(' :
                arr.pop()
    if temp == True and not arr :
        print("YES")
    else :
        print("NO")
