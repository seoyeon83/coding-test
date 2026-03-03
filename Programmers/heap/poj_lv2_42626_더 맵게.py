'''
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해..
가장 낮은 두 음식을 섞어서 새로운 음식을 만든다

섞은 음식의 스코빌 지수 
= 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

모든 음식의 스코빌 지수를 K 이상으로 만들기 위해..
최대, 최소 원소를 빠르게 꺼낼 수 있는 것 => 최소힙

heap

근데 결국 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우도 찾아야 하는데..
그 경우는 어떻게 알지? => 원소가 1개 남은 경우
'''
import heapq 

def solution(scoville, K):
    heapq.heapify(scoville)

    answer = 0
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        n = a + b*2
        heapq.heappush(scoville, n)
        
        answer += 1
        
    return answer