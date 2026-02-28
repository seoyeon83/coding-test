def solution(m, n, puddles):
    graph = [[0]*(m+1) for _ in range(n+1)]
    graph[1][1] = 1

    for x in range(1, n+1):
        for y in range(1, m+1):
            if [y, x] in puddles or (x == 1 and y == 1):
                continue
            graph[x][y] = graph[x-1][y] + graph[x][y-1]
            
    return graph[n][m] % 1000000007

print(solution(3, 3, [[2,2]]))