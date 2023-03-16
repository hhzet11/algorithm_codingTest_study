def solution(people, limit):
    # 1차 시도 - 실패
    answer = 0
    cabin = 0
    people.sort(reverse = True)
    for i in range(len(people)) :
        cabin += people[i]
        val = i
        while cabin < limit :
            val += 1
            if val == len(people) :
                break
            if limit-cabin >= people[val] :
                cabin += people[val]
                people.pop(val)
                val -= 1
        answer += 1
        cabin = 0
        if len(people) == i+1 :
            break
    return answer

# 다른 사람 풀이 1
from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse=True))
    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            answer += 1
            people.pop()
            people.popleft()
        else:
            answer += 1
            people.popleft()
    if people:
        answer += 1

    return answer

# 다른 사람 풀이 2
def solution(people, limit):
    answer = 0
    people.sort()
    a = 0
    b = len(people) -1
    while a < b:
        if people[b] + people[a] <= limit :
            a+= 1
            answer += 1
        b -= 1
    return len(people) - answer