import sys
input = sys.stdin.readline
n = int(input())
ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x): # 인덱스가 행, row[n]값이 현재 퀸의 열 위치
        # 열이 같거나, 대각선이 같으면 False
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False # 대각선이 같은 경우 두 좌표에서 행-행 = 열-열이 같으면 두개는 대각선 상에 위치함
    return True

def n_queens(x):
    global ans
    if x == n : # n번째 줄까지 맞는게 있어서 다 돌았다는 의미로 횟수 하나 증가
        ans += 1
        return
    else:
        # 각 행에 퀸 놓기
        for i in range(n): # i는 열번호 0~n까지 옮겨가면서 유망한 곳 찾기
            row[x] = i
            if is_promising(x): #행, 열, 대각선 체크하고 True면 백트래킹 안하고 진행
                n_queens(x+1)
n_queens(0)
print(ans)