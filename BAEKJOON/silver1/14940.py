# 쉬운 최단거리
import sys;input=sys.stdin.readline
from collections import deque

n, m = map(int, input().split()) # 세로, 가로
graph = [list(map(int, input().split())) for _ in range(n)]
# 상하좌우 방향
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
visited = [[-1]*m for _ in range(n)]
    
def bfs(a, b):
  q = deque() 
  q.append((a, b))
  visited[a][b] = 0
  
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if visited[nx][ny] == -1:
        if graph[nx][ny] == 0: # 갈 수 없는 땅
          visited[nx][ny] == 0
        elif graph[nx][ny] == 1: # 갈 수 있는 땅
          visited[nx][ny] = visited[x][y] + 1
          q.append((nx, ny))
          
for i in range(n):
  for j in range(m):
    if graph[i][j] == 2:
      bfs(i, j)

# 결과 출력
for i in range(n):
  for j in range(m):
    print(0 if graph[i][j] == 0 else visited[i][j], end=' ')
  print()