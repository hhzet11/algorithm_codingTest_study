# 1차 풀이 - 성공
def solution(n, wires):
    cut = n
    lenW = len(wires)
    for wire in wires :
        t1, t2 = [wire[0]], [wire[1]]
        for w in wires:
            if wire[0] == w[0] and wire[1] == w[1] :
                continue
            elif w[0] in t1 :
                t1.append(w[1])
            elif w[1] in t1 :
                t1.append(w[0])
            elif w[0] in t2 :
                t2.append(w[1])
            elif w[1] in t2 :
                t2.append(w[0])
            else :
                wires.append(w)
        cut = min(cut, abs(len(t1) - len(t2)))
        wires = wires[:lenW]
    return cut