def solution(n, arr1, arr2):
    # 1차 풀이 - 성공
    answer = []
    for i, j in zip(arr1, arr2):
        bin1 = list(map(int, format(i, 'b')))
        bin2 = list(map(int, format(j, 'b')))
        if len(bin1) < n :
            bin1 = [0] * (n - len(bin1)) + bin1
        if len(bin2) < n :
            bin2 = [0] * (n - len(bin2)) + bin2
        result = ''
        for x, y in zip(bin1, bin2):
            if x == 0 and y == 0 :
                result += ' '
            else :
                result += '#'
        answer.append(result)
    return answer

    # 다른 사람 풀이
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer