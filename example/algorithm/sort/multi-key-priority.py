# 우선순위가 여러 개일 때: 튜플 정렬 or heapq or lambda
import heapq


def pick_target(dist, candidates):
    # candidates: [(r, c), ... ], dist: bfs 결과
    best_key = None
    for r, c in candidates:
        if dist[r][c] == -1:
            continue
        key = (dist[r][c], r, c)
        if best_key is None or key < best_key:
            best_key = key
    return best_key

# 간결하게 표현 가능
def pick_target_short(dist, candidates):
    reachable = [(r, c) for r, c in candidates if dist[r][c] != -1]
    target = min(reachable, key=lambda p: (dist[p[0]][p[1]], p[0], p[1])) if reachable else None
    return target

import heapq

# heapq는 처리하는 도중 새 후보가 계속 추가되고 매번 회선을 꺼내야 하는 경우 (다익스트라, 우선순위 큐 등)
def heap_example():
    h = []
    heapq.heappush(h, (3, 0, 1))
    heapq.heappush(h, (1, 2, 2))
    heapq.heappush(h, (1, 0, 5))
    return heapq.heappop(h)

