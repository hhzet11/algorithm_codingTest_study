# 1차 풀이 - 성공
import math
def solution(fees, records):
    answer = []
    cars = {}
    for r in records:
        t, car, state = r.split()
        h, m = map(int, t.split(':'))
        if car not in cars:
            cars[car] = []
        cars[car].append(h * 60 + m)

    for c in list(cars.values()):
        if len(c) % 2 != 0:
            c.append(23 * 60 + 59)
        for t in range(len(c) // 2):
            c[t] = c[t + 1] - c[t]
            c.remove(c[t + 1])

    for c in cars:
        cars[c] = sum(cars[c])
        if cars[c] < fees[0]:
            cars[c] = fees[1]
        else:
            cars[c] = fees[1] + math.ceil((cars[c] - fees[0]) / fees[2]) * fees[3]

    return list(dict(sorted(cars.items())).values())