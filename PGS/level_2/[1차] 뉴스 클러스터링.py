# 1차 풀이 - 성공
import math
def solution(str1, str2):
    answer = 0
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1)]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1)]
    A, B = [],[]
    for i in str1 :
        if i.isalpha():
            A.append(i)
    for i in str2 :
        if i.isalpha():
            B.append(i)
    len_A, len_B = len(A), len(B)
    if len_A == 0 and len_B == 0 :
        return 65536
    else :
        inter = 0
        for i in A :
            if i in B :
                inter += 1
                B.remove(i)
        similarity = inter / (len_A + len_B - inter)
        return math.trunc(similarity * 65536)

# 다른 사람 풀이
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2) #교집합
    hap = set(str1) | set(str2) #합집합

    if len(hap) == 0 :
        return 65536

    # 중복 다시 세기
    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)
