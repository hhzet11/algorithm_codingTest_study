# 2차 풀이 - 성공
import re
def solution(files):
    answer = {}
    for file in files:
        num = []
        answer[file] = []
        start = 0
        for i, f in enumerate(file):
            if len(num) == 0 and f.isdigit():
                answer[file].append(file[:i])
                start = i
                num.append(f)
                if i == len(file) - 1:
                    answer[file].append(file[i:])
            elif f.isdigit() and i == len(file) - 1:
                answer[file].append(file[start:])
            elif f.isdigit():
                num.append(f)
            elif len(num) > 0 and f.isalpha():
                answer[file].append(file[start:i - 1])
                answer[file].append(file[i - 1:])
                break

    split = list(answer.values())
    split.sort(key=lambda x: [x[0].lower(), int(x[1])])

    return ["".join(s) for s in split]

# 다른 사람 풀이
import re
def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b


import re
def solution(files):
    def key_function(fn):
        head,number,tail = re.match(r'([a-z-. ]+)(\d{,5})(.*)',fn).groups()
        return [head,int(number)]
    return sorted(files, key = lambda x: key_function(x.lower()))