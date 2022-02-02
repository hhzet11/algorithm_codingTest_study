x, y, w, h = map(int, input().split())
result = []
if w/2 >= x : result.append(x)
else : result.append(w-x)

if h/2 >= y : result.append(y)
else : result.append(h-y)

print(min(result))
