'''
출발은 상근이네
맥주  한 박스에는 맥주 * 20
50미터에 한 병씩 마신다
0미터, 49미터, 98미터, ...
맥주 파는 편의점 개수 n

편의점에 들러서 빈 병은 버리고 새 맥주 병을 살 수 있지만 최대 20개까지 소지할 수 있다 
편의점을 나선 직후에도 50미터 가기 전에 맥주 한 병을 마셔야 한다

중간에 맥주가 바닥나서 더 이동할 수 없으면 sad, 도착하면 happy 

-32768 ≤ x, y ≤ 32767

1 = 1미터

dfs냐 bfs냐 ... bfs로 구현

맥주 한 박스로 갈 수 있는 최대 길이 = 1000미터

정점과 간선
정점은 집, 편의점, 페스티벌
정점 간 이동할 수 있는 간선은 1000미터 이하라면 간선이 존재한다고 볼 수 있다

서로 거리를 미리 계산해서 인접 리스트로 만들어 두거나 그때그때 거리를 계산해도 된다
'''
import sys 
from collections import deque


def get_distance(a, b):
    ax, ay = a
    bx, by = b

    return abs(ax - bx) + abs(ay - by)

def bfs(start, locations):

    visited = set()
    # 상근이네 enq
    queue = deque([start])
    
    while(queue):
        loc = queue.popleft()
        visited.add(loc)

        if loc == locations[-1]:
            return "happy"
        
        for location in locations:
            if location not in visited and get_distance(loc, location) <= 1000:
                queue.append(location)

    return "sad"

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    # 상근이네 
    start = tuple(map(int, sys.stdin.readline().split()))
    # 0~N-1: 편의점 N: 펜타포트
    locations = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N+1)]
    print(bfs(start, locations))

