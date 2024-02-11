from copy import deepcopy
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def left(board):
    for i in range(n):
        cursor = 0
        for j in range(1, n):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0 #현재칸 0으로 비우기
                if board[i][cursor] == 0 : # 비어있으면 옮긴다
                    board[i][cursor] = tmp
                elif board[i][cursor] == tmp : #같으면 합치기
                    board[i][cursor] += tmp
                    cursor += 1
                else : #비어있지도 않고, 같은 값도 아니면
                    cursor += 1 # pass
                    board[i][cursor] = tmp # 바로 옆에 붙임
    return board
def right(board):
    for i in range(n):
        cursor = n-1
        for j in range(n-2, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0  # 현재칸 0으로 비우기
                if board[i][cursor] == 0:  # 비어있으면 옮긴다
                    board[i][cursor] = tmp
                elif board[i][cursor] == tmp:  # 같으면 합치기
                    board[i][cursor] += tmp
                    cursor -= 1
                else:  # 비어있지도 않고, 같은 값도 아니면
                    cursor -= 1  # pass
                    board[i][cursor] = tmp  # 바로 옆에 붙임
    return board
def up(board):
    for j in range(n):
        cursor = 0
        for i in range(1, n):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0  # 현재칸 0으로 비우기
                if board[cursor][j] == 0:  # 비어있으면 옮긴다
                    board[cursor][j] = tmp
                elif board[cursor][j] == tmp:  # 같으면 합치기
                    board[cursor][j] += tmp
                    cursor += 1
                else:  # 비어있지도 않고, 같은 값도 아니면
                    cursor += 1  # pass
                    board[cursor][j] = tmp  # 바로 옆에 붙임
    return board
def down(board):
    for j in range(n):
        cursor = n-1
        for i in range(n-2, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0  # 현재칸 0으로 비우기
                if board[cursor][j] == 0:  # 비어있으면 옮긴다
                    board[cursor][j] = tmp
                elif board[cursor][j] == tmp:  # 같으면 합치기
                    board[cursor][j] += tmp
                    cursor -= 1
                else:  # 비어있지도 않고, 같은 값도 아니면
                    cursor -= 1  # pass
                    board[cursor][j] = tmp  # 바로 옆에 붙임
    return board

def dfs(board, cnt):
    if cnt == 5 :
        return(max(map(max, board))) #2차원 요소 중 가장 큰 값 반환
    return max(dfs(up(deepcopy(board)), cnt +1), dfs(down(deepcopy(board)), cnt +1), dfs(left(deepcopy(board)), cnt +1), dfs(right(deepcopy(board)), cnt +1))
print(dfs(board, 0))