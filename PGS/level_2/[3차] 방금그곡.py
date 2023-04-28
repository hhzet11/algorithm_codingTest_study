# 1차 풀이 - 성공
def solution(m, musicinfos):
    answer = []
    sound = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a'}
    for info in musicinfos:
        start, end, title, sheet = info.split(',')
        start = list(map(int, start.split(':')))
        end = list(map(int, end.split(':')))
        time = (end[0] - start[0]) * 60 + (end[1] - start[1])

        for s in sound.keys():
            sheet = sheet.replace(s, sound[s])
            m = m.replace(s, sound[s])

        sheet = sheet * (time // len(sheet)) + sheet[:time % len(sheet)]
        if m in sheet:
            answer.append([time, title])

    if len(answer) > 1:
        answer.sort(key=lambda x: x[0], reverse=True)
        return answer[0][1]
    elif len(answer) == 0:
        return '(None)'
    else:
        return answer[0][1]