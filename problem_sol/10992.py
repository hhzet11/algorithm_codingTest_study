n = int(input())
for i in range(1, n+1):
    if i == n:
        print("*" * (2*i-1))
    elif i == 1:
        print(" " * (n-i) + "*")
    else:
        print(" " * (n-i) + "*" + " ")