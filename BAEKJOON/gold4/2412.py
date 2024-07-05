# 암벽 등반
import sys;input=sys.stdin.readline
from collections import deque

n, T = map(int, input().split())
holds = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*1000000 for _ in range(T)]

sx, sy = 0, 0
cnt = 0

def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    
    while q:
        x, y = q.popleft()
        if abs(sx - x) <= 2 and abs(sy - y) <= 2 and not visited[x][y]:
            q.append((x, y))
            sx, sy = x, y
            visited[x][y] = True