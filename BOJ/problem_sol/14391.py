import sys
input = sys.stdin.readline
n, m = map(int, input().split())

paper = []
for _ in range(m) :
    paper.append(list(map(int, input().rstrip())))

ans = []
# 비트마스크로 2^(n*m)의 경우의 수를 따져본다
for i in range(1 << n*m) :
    total = 0
    # 가로합 계산
    for row in range(n) :
        rowsum = 0
        for col in range(m):
            # idx는 2차원 행렬을 1줄로 만들었을 때의 인덱스
            idx = row*m + col #idx는 오른쪽으로 늘어나면서 검사

            # i번째 경우의 수에서 idx번째 요소가 있으면, 즉 이어져있는 수면 더한다.
            if i & (1 << idx) != 0: #(0이 아니면 가로로 더한다)
                rowsum = rowsum * 10 + paper[row][col]
            # 세로일 때, 앞에서 나온 수를 total에 더하고 초기화
            else:
                total += rowsum
                rowsum = 0
        total += rowsum
    # 세로합 계산
    for col in range(m):
        colsum = 0
        for row in range(n):
            # row가 증가하는 방향 즉 위에서 아래로 한칸씩 늘리며, 0이면 10의 자릿수 맞춰주고 1이면 자릿수 초기화
            idx = row*m + col
            # 세로일 때, 즉 0이면 이전에 나온 숫자를 왼쪽으로 한칸 씩 밀며 1의 자릿수로 들어감
            if i & (1 << idx) == 0 : #0이면 세로로 더한다
                colsum = colsum * 10 + paper[row][col]
            # 가로일 때 앞에서 나온수를 total에 더하고, 초기화
            else :
                total += colsum
                colsum = 0
        total += colsum
    ans.append(total)
print(max(ans))