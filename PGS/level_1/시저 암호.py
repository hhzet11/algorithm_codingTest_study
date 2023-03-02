def solution(s, n):
    # 1차 시도 - 실패
    asc = []
    for i in list(s) :
        if i == ' ':
            asc.append(i)
        else :
            if i == 'z':
                num = 96
            elif i == 'Z' :
                num = 64
            else :
                num = ord(i)
            asc.append(chr(num + n))
    return ''.join(i for i in asc)

    # 2차 시도 - 성공
    asc = []
    for i in list(s):
        if i == ' ':
            asc.append(i)
        else:
            num = ord(i)
            if num < 91 and num + n > 90:
                num = num + n - 26
            elif 95 < num < 123 and num + n > 122:
                num = num + n - 26
            else:
                num += n
            asc.append(chr(num))
    return ''.join(i for i in asc)

    # 다른사람 코드
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return "".join(s)