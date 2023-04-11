# 1차풀이 - 실패 : 시간초과1
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0 for _ in range(bridge_length)]
    while len(truck_weights) > 0 :
        truck = truck_weights[0]
        bridge.pop()
        if len(bridge) < bridge_length and sum(bridge) + truck <= weight :
            bridge.insert(0, truck)
            truck_weights.pop(0)
        else :
            bridge.insert(0, 0)
        time += 1
    time += len(bridge) - bridge.index(truck)
    return time

# 2차 풀이 - 성공
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0 for _ in range(bridge_length)]
    while len(truck_weights) > 0 :
        truck = truck_weights[0]
        bridge.pop(0)
        if sum(bridge) + truck <= weight :
            bridge.append(truck) # insert보다 append가 시간 빠름
            truck_weights.pop(0)
        else :
            bridge.append(0)
        time += 1
    return time + len(bridge)