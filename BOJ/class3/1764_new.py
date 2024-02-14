n, m = map(int, input().split())
non_seen, non_heard = set(), set()
for _ in range(n):
    non_seen.add(input())
for _ in range(m):
    non_heard.add(input())
result = list(non_seen & non_heard)
result.sort()
print(len(result))
for i in result:
    print(i)