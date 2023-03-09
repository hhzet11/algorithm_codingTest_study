def solution(keymap, targets):
    # 1차 풀이 - 성공
    answer = []
    character = {}
    for key in keymap :
        for i in key :
            if i not in character.keys() or character[i] > key.index(i) :
                character[i] = key.index(i)
    for key in targets :
        sum = 0
        for i in key :
            if i in character :
                sum += character[i] + 1
            else :
                sum = -1
                break
        answer.append(sum)
    return answer

    # 다른 사람 풀이
    answer = []
    hs = {}
    for k in keymap:
        # index 활용 시에는 enumerate 사용!
        for i, ch in enumerate(k):
            hs[ch] = min(i + 1, hs[ch]) if ch in hs else i + 1

    for i, t in enumerate(targets):
        ret = 0
        for ch in t:
            if ch not in hs:
                ret = - 1
                break
            ret += hs[ch]
        answer.append(ret)

    return answer