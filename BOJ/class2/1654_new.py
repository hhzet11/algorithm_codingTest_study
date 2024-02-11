import sys

k, n = map(int, sys.stdin.readline().split())
lan = []
for i in range(k):
    lan.append(int(sys.stdin.readline()))

start = 1
end = max(lan)

while start <= end : #이분탐색 완료 전까지
    mid = (start + end) // 2
    cnt = 0

    for i in lan :
        cnt += i // mid

    if cnt >= n: #n개보다 많은 경우 >> 즉, 더 큰 길이가 가능한 경우
        start = mid + 1
    else : #n개보다 적은 경우 >> 즉, 더 큰 길이가 줄어들어야 하는 경우
        end = mid - 1

print(end)