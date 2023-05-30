from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridgeWeight = 0
    bridge_on_trucks = deque([0] * bridge_length)
    waiting = deque(truck_weights)

    while len(waiting) or bridgeWeight > 0:
        b = bridge_on_trucks.popleft()
        bridgeWeight -= b

        if len(waiting) and bridgeWeight + waiting[0] <= weight:
            a = waiting.popleft()
            bridgeWeight += a
            bridge_on_trucks.append(a)
        else:
            bridge_on_trucks.append(0)
        
        answer += 1

    return answer

# sum 시간복잡도 O(n)