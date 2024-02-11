while True:
    arr = input()
    a = []
    if arr == '.':
        break

    for i in arr:
        if i == '[' or i == '(':
            a.append(i)
        elif i == ']':
            if len(a) != 0 and a[-1] == '[':
                a.pop()
            else:
                a.append(i)
                break
        elif i == ')':
            if len(a) != 0 and a[-1] == '(':
                a.pop()
            else:
                a.append(i)
                break
    if len(a) == 0:
        print('no')
    else:
        print('yes')