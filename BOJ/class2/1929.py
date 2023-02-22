'''
m, n = map(int, input().split())
cnt = []
for i in range(m, n+1):
    check = 0
    for j in range(2, int(num**0.5)+1):
        if i % j == 0:
            check = 1
    if check == 0 :
        cnt.append(i)

for i in range(len(cnt)):
    print(cnt[i])

'''
# 소수 검사시 2부터 i까지가 아닌, 2부터 i의 제곱근까지만 검사 -> 시간 초과 피함
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)
