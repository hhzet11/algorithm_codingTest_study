def solution(s):
    # 1차 풀이 - 성공
    answer = True
    stack = []
    for i in s :
        stack.append(i)
        if len(stack) > 1 and stack[-2] == '(' and stack[-1] == ')':
            stack.pop()
            stack.pop()
    if len(stack) == 0 :
        return True
    else :
        return False