# 1차 풀이 - 실패
def solution(s):
    final = len(s)
    for length in range(1, len(s)):
        split = [s[i:i + length] for i in range(0, len(s), length)]
        answer, cnt = '', 1
        # print(split)
        for i in range(len(split) - 1):
            if split[i] == split[i + 1]:
                cnt += 1
            else:
                answer += str(cnt) + split[i]
                cnt = 1

            if i == len(split) - 2:
                answer += str(cnt) + split[i + 1]
            # print(answer)
        answer = answer.replace('1', '')
        if len(answer) <= final:
            final = len(answer)
    return final

# 다른 사람 풀이
def solution(s):
    result = []
    if len(s) == 1:
        return 1
    for i in range(1, (len(s) // 2) + 1):
        b = ''
        cnt = 1
        tmp = s[:i]
        # print(tmp)
        for j in range(i, len(s), i):
            if tmp == s[j:i + j]:
                cnt += 1
            else:
                if cnt != 1:
                    b = b + str(cnt) + tmp
                else:
                    b = b + tmp
                tmp = s[j:j + i]
                cnt = 1
        if cnt != 1:
            b = b + str(cnt) + tmp
        else:
            b = b + tmp

        result.append(len(b))
    return min(result)