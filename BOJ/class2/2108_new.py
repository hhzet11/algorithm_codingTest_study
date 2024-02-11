n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

r = []
# 산술평균
r.append(round(sum(arr) / n))
# 중앙값
r.append(arr[n // 2])

'''
counts = list(dict(Counter(arr)).items())
counts = sorted(counts, key = lambda x : (-x[1], x[0]))

if len(counts) > 1 and counts[0][0] == counts[1][0] :
    r.append(counts[1][0])
else :
    r.append(counts[0][0])
'''
# n의 범위가 500,000까지이므로 리스트 순회를 줄여야 함
# 하지만 정렬이 불가피하므로, 인덱싱을 활용
# 인덱싱은 시간복잡도가 O(1)이므로 내장함수 대신 사용
count = dict()
for i in arr:
    if i not in count :
        count[i] = 1
    else :
        count[i] += 1

# 최빈값
freq = max(count.values())
numb = []
for k, v in count.items():
    if v == freq:
        numb.append(k)

if len(numb) == 1 :
    r.append(numb[0])
else :
    r.append(sorted(numb)[1])

# 범위
r.append(arr[-1] - arr[0])

for i in r:
    print(i)
