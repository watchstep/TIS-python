# 상범 빌딩
import sys;input=sys.stdin.readline
from collections import deque

def bfs(a, b, c):
    q = deque()
    q.append([a, b, c])
    visited[a][b][c] = 1
    
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if nx < 0 and nx >= L and ny < 0 and ny >= R and nz < 0 and nz >= C:
                continue
            if graph[nx][ny][nz] == 'E':
                print(f"Escaped in {visited[x][y][z]} minute(s).")
                return
            if graph[nx][ny][nz] == '.' and visited[nx][ny][nz] == 0:
                visited[nx][ny][nz] = visited[x][y][z] + 1
                q.append([nx, ny, nz])
    print("Trapped!")

for i in range(L):
    for j in range(R+1):
        for h in range(C):
            bfs(i, j, h)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]           
while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    graph = [[list(input().rstrip()) for _ in range(R+1)] for _ in range(L)]
    visited = [[[0]*C]*(R+1) for _ in range(L)]