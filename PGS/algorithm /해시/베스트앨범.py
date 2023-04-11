# 1차 풀이 - 성공
import itertools
def solution(genres, plays):
    cnt = {}
    for g, p in zip(genres, plays):
        if g not in cnt:
            cnt[g] = p
        else:
            cnt[g] += p
    cnt = dict(sorted(cnt.items(), key=lambda x: x[1], reverse=True))

    playIdx = {}
    for c in list(cnt.keys()):
        playIdx[c] = {}
    for i, p in enumerate(plays):
        playIdx[genres[i]][i] = p

    play = []
    for p in playIdx.values():
        play.append(dict(sorted(p.items(), key=lambda x: (-x[1], x[0]))))

    answer = []
    for p in play:
        if len(p) == 1:
            answer.append(p.keys())
        else:
            answer.append(list(p.keys())[:2])

    return list(itertools.chain(*answer))

# 다른 사람 풀이
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer