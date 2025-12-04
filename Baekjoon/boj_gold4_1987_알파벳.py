'''
세로 R칸, 카로 C칸
새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀있는 알파벳과는 달라야 한다
같은 알파벳이 적힌 칸을 두 번 지날 수 없다

백트래킹...같은데...

알고리즘은 알았으나 어떻게 풀어야할지에 관한 건 스스로 생각해내지 못함
gemini의 도움으로 풀었는데 조만간 다시 혼자 힘으로 풀어볼 것!

visited를 set()으로 하는 게 아니라 배열로 설정
백트래킹이므로, 재귀함수 호출 후 원상태로 돌려내는 과정 필요
ans를 전역변수로 설정하고, cnt로 개수를 전달하면서 cnt가 갱신되어 새롭게 함수를 호출할 때마다 ans의 값을 갱신
'''

import sys 


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ans = 1

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C and not visited[ord(graph[nx][ny]) - 65]:
            visited[ord(graph[nx][ny]) - 65] = True
            dfs(nx, ny, cnt + 1)
            visited[ord(graph[nx][ny]) - 65] = False

R, C = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline()) for _ in range(R)]
visited = [False] * 26
visited[ord(graph[0][0]) - 65] = True

dfs(0, 0, 1)
print(ans)