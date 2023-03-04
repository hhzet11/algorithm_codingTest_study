def solution(answers):
    # 1차 풀이 - 실패
    answer = {}
    players = [[1, 2, 3, 4, 5],
              [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    idx = 1
    final = []
    for player in players :
        if len(player) < len(answers) :
            player = player * (len(answers) // len(player)) + player[:(len(answers) % len(player))]
        cnt = 0
        for i, j in zip(player, answers) :
            if i-j == 0 :
                cnt += 1
        answer[idx] = cnt
        idx += 1
    answer = dict(sorted(answer.items(), key = lambda x: x[1], reverse = True))
    for k in answer :
        if answer[k] != 0:
            final.append(k)
    return final

    # 다른 사람 풀이
    player1 = [1, 2, 3, 4, 5]
    player2 = [2, 1, 2, 3, 2, 4, 2, 5]
    player3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []
    for idx, answer in enumerate(answers):
        if answer == player1[idx % len(player1)]:
            score[0] += 1
        if answer == player2[idx % len(player2)]:
            score[1] += 1
        if answer == player3[idx % len(player3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx + 1)
    return result