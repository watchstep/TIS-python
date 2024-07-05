# 알고스팟
import sys;input=sys.stdin.readline
from collections import deque

M, N = map(int, input().split()) # 가로, 세로
graph = [list(map(int, list(input().strip()))) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [-1, 1, 0, 0]
visited = [[0]*M for _ in range(N)]
cnt = 0

def dfs(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if graph[nx][ny] and not visited[nx][ny]:
            cnt = min(cnt, dfs(nx, ny) + 1)
            visited[x][y] = 0
            dfs(nx, ny)
    return cnt

res = 0
for i in range(N):
    for j in range(M):
        if graph[i][j]:
            res = min(res ,dfs(i, j))
            
            