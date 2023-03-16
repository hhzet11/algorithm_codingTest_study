def solution(n, words):
    for w in range(len(words)) :
        # 1차 시도 - 실패 85
        #if w > 0 and (words[w-1][-1] != words[w][0] or words.count(words[w]) > 1) :
        # 2차 시도 - 성공
        if w > 0 and (words[w - 1][-1] != words[w][0] or words[w] in words[:w]):
            return [(w%n)+1, (w//n)+1]
            break
    return [0, 0]