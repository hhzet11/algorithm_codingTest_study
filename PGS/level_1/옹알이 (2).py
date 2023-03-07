import re
def solution(babbling):
    # 1차 풀이 - 실패
    answer = 0
    overlap = ['ayaaya', 'yeye', 'woowoo', 'mama']
    result = []
    for bab in babbling :
        for i in overlap :
            if i in bab:
                babbling.remove(bab)
    for bab in babbling :
        result.append(re.sub("aya|ye|woo|ma", "", bab))
    for i in result :
        if len(i) == 0 :
            answer += 1
    return answer

    # 다른 사람 풀이
    count = 0
    babble = ["aya", "ye", "woo", "ma"]
    for utter in babbling:
        for text in babble:
            if text * 2 not in utter:
                utter = utter.replace(text, ' ')
        if utter.strip() == '':
            count += 1
    return count

