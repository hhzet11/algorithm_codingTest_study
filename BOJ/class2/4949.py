while True :
    str = list(input())
    if str[0] == '.':
        break
    paranthesis = []
    temp = True
    for i in str :
        if i == '(' or i =='[':
            paranthesis.append(i)
        elif i == ')':
            if not paranthesis or paranthesis[-1] == '[':
                temp = False
                break
            elif paranthesis[-1] == '(':
                paranthesis.pop()
        elif i == ']':
            if not paranthesis or paranthesis[-1] == '(':
                temp = False
                break
            elif paranthesis[-1] == '[':
                paranthesis.pop()
    if temp == True and not paranthesis :
        print('yes')
    else :
        print('no')