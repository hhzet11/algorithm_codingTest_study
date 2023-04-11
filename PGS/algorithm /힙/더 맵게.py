# 1차 풀이 - 실패 : 효율성 테스트 시간초과
def solution(scoville, K):
    answer = 0
    scoville.sort()
    while len(scoville) >= 2 and scoville[0] < K :
        new = scoville[0] + (scoville[1] * 2)
        scoville.pop(0)
        scoville.pop(0)
        scoville.append(new)
        scoville.sort()
        answer += 1
    if scoville[0] < K :
        return -1
    else :
        return answer

# 다른 사람 풀이 : heapq 적용
import heapq
def solution(scoville, K):
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)

    cnt = 0
    while heap[0] < K:
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        cnt += 1

        if len(heap) == 1 and heap[0] < K:
            return -1
    return cnt