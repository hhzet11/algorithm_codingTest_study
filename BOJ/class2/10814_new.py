n = int(input())
apply = []
for i in range(n):
    age, name = map(str, input().split())
    apply.append([int(age), name])
apply.sort(key = lambda x: x[0])
for i in apply:
    print(i[0], i[1])