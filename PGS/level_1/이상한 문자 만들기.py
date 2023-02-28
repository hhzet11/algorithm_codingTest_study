def solution(s):
    # 1차 풀이 - 실패
    answer = []
    for x in s.split():
        answer.append(list(x))

    final = ''
    for word in answer:
        for l in range(len(word)):
            if l % 2 == 0:
                final += word[l].upper()
            else:
                final += word[l].lower()
        final += ' '
    return final[:-1]

    # 다른 사람 풀이
def solution(s):
    answer = ''
    new_list = s.split(' ')
    for i in new_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer+= ' '
    return answer[0:-1]