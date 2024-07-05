# 말이 되고픈 원숭이
import sys;input=sys.stdin.readline
from collections import deque

K = int(input())
W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
hdx = [-2, -1, 1, 2, -2, -1, 1, 2]
hdy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs():
    global K
    q = deque()
    q.append((0, 0, K))
    visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
    
    while q:
        x, y, k = q.popleft()
        if (x == H - 1) and (y == W - 1):
            return visited[x][y][k]
        if k > 0:
            for i in range(8):
                nx, ny = x + hdx[i], y + hdy[i]
                if (nx < 0) or (nx >= H) or (ny < 0) or (ny >= W):
                    continue
                if not visited[nx][ny][k-1] and not graph[nx][ny]:
                    visited[nx][ny][k-1] = visited[x][y][k] + 1
                    q.append((nx, ny, k-1))
        
    
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (nx < 0) or (nx >= H) or (ny < 0) or (ny >= W):
                continue
            if not visited[nx][ny][k] and not graph[nx][ny]:
                visited[nx][ny][k] = visited[x][y][k] + 1
                q.append((nx, ny, k))
    
    return -1
                    
res = bfs()
print(res)


