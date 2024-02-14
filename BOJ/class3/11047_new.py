n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse = True)

answer = 0
for c in coin:
    if k == 0 :
        break
    if c <= k:
        answer += k // c
        k = k % c
print(answer)