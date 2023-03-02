def solution(s):
    answer = ''
    num_dict = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3',
                'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7',
                'eight' : '8', 'nine' : '9'}
    # 1차 풀이 - 성공
    num_str = ''
    for i in range(len(s)) :
        if s[i] in num_dict.values():
            answer += s[i]
        else :
            num_str += s[i]
            if num_str in num_dict.keys() :
                answer += num_dict[num_str]
                num_str = ''
    return int(answer)

    # 다른 사람 풀이
    answer = s
    for key, value in num_dict.items():
        answer = answer.replace(key, value)
    return int(answer)
