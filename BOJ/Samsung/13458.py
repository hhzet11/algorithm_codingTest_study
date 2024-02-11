# 1차 실패
# 2차 성공
n = int(input())
room = list(map(int, input().split()))
b, c = map(int, input().split())

result = n
for r in room :
    r -= b
    if r > 0 : # r-b를 하고 0보다 큰지 고려해야 하는 것이 중요!
        if r % c: # 코드 간단히 하는 팁
            result += (r // c) + 1
        else:
            result += (r // c)
print(result)