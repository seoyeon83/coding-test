# from collections import deque


# def solution(bridge_length, weight, truck_weights):
#     answer = 0
    
#     truck_weights.reverse()
#     bridge = deque()
    
#     while truck_weights or bridge:
#         # 다리 현재 상황 파악
#         # 1. 다 건넌 트럭 처리
#         # 2. 무게 확인
#         total_weight = 0
#         for _ in range(len(bridge)):
#             truck, time = bridge.popleft()
#             time += 1
#             if time < bridge_length:
#                 bridge.append((truck, time))
#                 total_weight += truck
        
#         # 트럭이 다리에 더 올라갈 수 있으면 올리기
#         if truck_weights and total_weight + truck_weights[-1] <= weight and len(bridge) < bridge_length:
#             truck = truck_weights.pop()
#             bridge.append((truck, 0))
        
#         answer += 1

#     return answer


# print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))


'''
근데 다른 사람들 풀이를 보니 0을 집어 넣어서 시간 계산을 안해도 되게 만든다~ 는 걸 봤는데..
코드를 대충 봐도 이해가 잘 되지는 않아서 한 번 내가 머리 써보면서 도전해보기로 함
=> 성공!! 와 이런 게 가능하구나.. 놀랍네
'''

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    truck_weights.reverse()
    bridge = deque([0]*bridge_length)
    total_weight = 0
    
    # 토탈 weight를 두고..
    while truck_weights or total_weight:
        total_weight -= bridge.popleft()

        # 트럭이 브릿지에 올릴 수 있으면 올린다
        if truck_weights and total_weight + truck_weights[-1] <= weight:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        else: # 없으면 0 추가
            bridge.append(0)

        answer += 1

    return answer

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
