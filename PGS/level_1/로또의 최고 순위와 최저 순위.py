def solution(lottos, win_nums):
    # 1차 풀이 - 성공
    answer = []
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    cnt, win = 0, 0
    for i in lottos:
        if i == 0:
            cnt += 1
        if i in win_nums:
            win += 1
    answer.append(rank[win])
    if rank[win] - cnt > 0:
        answer.append(rank[win] - cnt)
    else:
        answer.append(1)

    return answer[::-1]

    # 다른 사람 풀이
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans], rank[ans]
