text = list(input())
x = 0
while True :
    if x+10 < len(text):
        print(''.join(map(str, text[x:x+10])))
    else :
        print(''.join(map(str, text[x:])))
        break
    x += 10
