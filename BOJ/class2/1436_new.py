n = int(input())
title = [0]
for i in range(2700000):
    if len(title) == 10001 :
        break
    if '666' in str(i) :
        title.append(i)
print(title[n])
