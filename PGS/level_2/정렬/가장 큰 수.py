# 1차시도 - 실패 : 시간 초과
from itertools import permutations
def solution(numbers):
    answer = ''
    for i in permutations(numbers, len(numbers)):
        i = list(map(str, i))
        num = ''.join(i)
        if answer < num:
            answer = num
    return answer

# 다른 사람 풀이
def solution(numbers):
    numbers_str = [str(num) for num in numbers]
    # 원소의 최대값 1000 이므로 *3으로 3자리 이상의 수 만들어서 정렬
    numbers_str.sort(key=lambda num: num*3, reverse=True)
    return str(int(''.join(numbers_str)))

