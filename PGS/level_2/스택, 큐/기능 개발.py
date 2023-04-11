def solution(progresses, speeds):
    # 1차 플이 - 성공
    answer, final = [], []
    for i, p in enumerate(progresses):
        p = 100 - p
        if p % speeds[i] == 0:
            p //= speeds[i]
        else:
            p = p // speeds[i] + 1
        answer.append(p)

    num, cnt = answer[0], 1
    for a in answer[1:]:
        if num < a:
            num = a
            final.append(cnt)
            cnt = 1
        else:
            cnt += 1
    final.append(cnt)
    return final

# 다른 사람 풀이
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]