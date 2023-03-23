def solution(record):
    # 1차 풀이 - 성공
    answer = []
    records = []
    id = {}
    for r in record :
        r = list(map(str, r.split()))
        records.append(r)
        if r[0] != 'Leave':
            id[r[1]] = r[2]
    for r in records :
        if r[0] == 'Enter' :
            answer.append('{}님이 들어왔습니다.'.format(str(id[r[1]])))
        elif r[0] == 'Leave' :
            answer.append('{}님이 나갔습니다.'.format(str(id[r[1]])))
    return answer

# 다른 사람 풀이
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer