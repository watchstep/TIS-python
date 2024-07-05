# 단지번호붙이기
import sys;input=sys.stdin.readline
from collections import deque

N = int(input())
graph = [list(input().strip()) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0]*N for _ in range(N)]
def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1
    home = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if (not visited[nx][ny]) and (graph[nx][ny] == '1'):
                q.append((nx, ny))
                visited[nx][ny] = 1
                home += 1
                
    return home

res = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == '1' and not visited[i][j]:
            res.append(bfs(i, j))

print(len(res))  
print(*sorted(res), sep='\n')