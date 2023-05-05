# 그림
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 재귀 깊이 설정

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0] # 좌, 우
dy = [0, 0, -1, 1] # 상, 하


area = 0
def dfs(x, y):
  global area
  # 범위 벗어났을 때
  if x < 0 or x >= n or y < 0 or y >= m:
    return False
  
  # 아직 방문 안했다면, (1이면)
  if graph[x][y]:
    area += 1
    graph[x][y] = 0 # 방문 처리 (0으로)
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      dfs(nx, ny)
    return True
  
  return False

areas = []
for i in range(n):
  for j in range(m):
    if dfs(i, j):
      areas.append(area)
      area = 0
      
print(len(areas))
print(max(areas) if len(areas) > 0 else 0)

# 다른 풀이 (bfs)
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0] # 좌, 우
dy = [0, 0, -1, 1] # 상, 하



def bfs(x, y):
  q = deque()
  area = 0
  q.append((x, y))
  graph[x][y] = 0 # 방문 처리
  area += 1
  
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위 넘어섰을 때
        continue
      if graph[nx][ny]:
        graph[nx][ny] = 0
        q.append((nx, ny))
        area += 1
        
  return area

areas = []

for i in range(n):
  for j in range(m):
    if graph[i][j]:
      areas.append(bfs(i, j))
      
print(len(areas))
print(max(areas) if len(areas) > 0 else 0)      
      