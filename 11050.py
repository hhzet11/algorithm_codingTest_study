n,k = map(int, input().split())
def fact(num):
    return fact(num-1) * num if num > 1 else 1

print(int(fact(n) / (fact(k) * fact(n-k))))