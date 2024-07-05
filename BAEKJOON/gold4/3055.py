# 탈출
import sys;input=sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
visited = [[False]*C for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    time = 0
    q = deque()
    q.append((sx, sy))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C or visited[nx][ny]:
                continue
            if arr[nx][ny] == "D":
                return time
            
            if arr[nx][ny] == "." or arr[nx][ny] == "S" and arr[x][y] == "*":
                arr[nx][ny] = "*" # 물 차게 됨
                visited[nx][ny] = True
                q.append((nx, ny))
            elif arr[nx][ny] == "." or arr[nx][ny] == "D" and arr[x][y] == "S":
                arr[nx][ny] = "S"
                visited[nx][ny] = True
                q.append((nx, ny))
                time += 1
                
    return "KAKTUS"

for i in range(R):
    for j in range(C):
        if arr[i][j] == "S": # 고슴도치
            print(bfs(i, j))
            