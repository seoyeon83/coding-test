'''
heapq

heapq.heappush(): 원소 삽입
heapq.heappop(): 원소 삭제(빼내기)

heapsort() => 힙에 넣었다가 빼는 것만으로도 O(NlogN)
'''

import heapq

# 힙 정렬 (최소 힙, 오름차순)
def heapsort(iterable):
    h = []          # 이게 힙
    result = []     # 정렬 결과
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result


# 힙 정렬 (최대 힙, 내림차순, 부호 임시 변경)
def heapsort_r(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


print(heapsort([1, 4, 6, 2, 3, 9, 10, 7, 8, 5]))
print(heapsort_r([1, 4, 6, 2, 3, 9, 10, 7, 8, 5]))