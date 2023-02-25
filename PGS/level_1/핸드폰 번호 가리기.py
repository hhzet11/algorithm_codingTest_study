def solution(phone_number):
    # 1차 풀이 성공
    return '*' * len(phone_number[:-4]) + phone_number[-4:]

    # 다른 사람 풀이
    return '*' * (len(phone_number)-4) + phone_number[-4:]