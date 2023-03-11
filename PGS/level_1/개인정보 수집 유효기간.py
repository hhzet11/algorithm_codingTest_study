def solution(today, terms, privacies):
    # 1차 시도 - 실패
    answer = []
    limit = {}
    today = today.replace('.', '')
    for i in terms:
        k, v = map(str, i.split())
        limit[k] = int(v)

    cnt = 1
    for pri in privacies:
        date, k = map(str, pri.split())
        date = list(map(int, date.split('.')))
        if limit[k] + date[1] > 12:
            date[0] += (limit[k] + date[1]) // 12
            date[1] = (limit[k] + date[1]) % 12
    else:
            date[1] += limit[k]

        for i in range(len(date)):
            if len(str(date[i])) < 2:
                date[i] = '0' + str(date[i])

        num = ''.join(str(i) for i in date)

        if int(num) <= int(today):
            answer.append(cnt)
        cnt += 1

    return answer