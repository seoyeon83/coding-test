from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    # 양방향 인접 그래프로 반환
    words.append(begin)
    graph = {word:list() for word in words}
    for w1 in words:
        for w2 in words:
            if w1 == w2: continue
            
            cnt = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    cnt += 1
            if cnt == 1:
                graph[w1].append(w2)
                
    # bfs로 최소 거리 탐색
    queue = deque([(begin, 0)])
    print(queue)
    visited = set([begin])
    while queue:
        n = queue.popleft()
        
        if n[0] == target:
            return n[1]
        
        for w in graph[n[0]]:
            if w not in visited:
                queue.append((w, n[1]+1))
                visited.add(w)
                    
    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))