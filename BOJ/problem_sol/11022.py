T = int(input())
for x in range(1, T+1):
    A, B = map(int, input().split())
    print("Case #{0}: {1} + {2} = {3}".format(x, A, B, A+B))