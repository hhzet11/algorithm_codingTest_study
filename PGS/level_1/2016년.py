def solution(a, b):
    # 1차 풀이 - 성공
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    num = sum(mon[:a-1]) + b
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    return day[num % 7]
