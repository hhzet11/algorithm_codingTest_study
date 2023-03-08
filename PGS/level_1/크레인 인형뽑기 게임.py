def solution(board, moves):
    # 1차 풀이 - 성공
    answer = 0
    container = []
    for i in moves :
        for j in range(len(board)):
            if board[j][i-1] > 0:
                container.append(board[j][i-1])
                board[j][i-1] = 0
                if len(container) > 1 and container[-1] == container[-2] :
                    answer += 2
                    container.pop()
                    container.pop()
                break
    return answer