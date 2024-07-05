# 아기 상어 2
import sys; input=sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 방향
dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 1, 0, -1, 1, 0, -1, 1]

q = deque()
def bfs():
  while q:
    x, y = q.popleft()
    for i in range(8):
      nx, ny = x + dx[i], y + dy[i]
      # 범위 넘어선 경우 
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      # 상어 없는 경우
      if not graph[nx][ny]:
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx, ny))


for i in range(n):
  for j in range(m):
    # 상어 있는 경우
    if graph[i][j]:
      q.append((i, j))

bfs()
print(max(map(max, graph))-1)
      
        