# 보물섬 
import sys;input=sys.stdin.readline
from collections import deque

H, W = map(int, input().split()) # 세로, 가로
graph = [list(input().strip()) for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited = [[0]*W for _ in range(H)]
    visited[a][b] = 1 # 시작점 방문 처리 해줘야함!
    cnt = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if graph[nx][ny] == "L" and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                cnt = max(cnt, visited[nx][ny])
                q.append((nx, ny))
    return cnt - 1 # 시작점 제외

res = 0
for i in range(H):
    for j in range(W):
        if graph[i][j] == "L":
            res = max(res, bfs(i, j))
            
print(res)

# PyPY로 해야 통과