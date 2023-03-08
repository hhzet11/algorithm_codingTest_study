def solution(s):
    # 1차 풀이 - 성공
    answer = 0
    word = []
    for i in s :
        word.append(i)
        if len(word) > 1 and word.count(word[0]) == len(word)//2 :
            word = []
            answer += 1
    if len(word) > 0 :
        answer += 1
    return answer