def solution(s):
    # 1차 풀이 - 성공
    if len(s) % 2 == 0:
        return s[len(s)//2 -1 : len(s)//2 +1]
    else:
        return s[len(s)//2]

    # 다른사람 풀이
    return str[(len(str) - 1) // 2: len(str) // 2 + 1]