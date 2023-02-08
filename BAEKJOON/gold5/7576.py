# 토마토
import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(N)]

# 왼, 오
dx = [-1, 1, 0, 0]
# 아래, 위
dy = [0, 0, -1, 1]

queue = deque()
for y in range(N):
  for x in range(M):
    if tomato[y][x] == 1:
      queue.append((y, x))        
      

while queue:
  y, x = queue.popleft()
  for i in range(4):
    ny = dy[i] + y
    nx = dx[i] + x
    # 범위 넘어섰을 때
    if 0 <= ny < N and 0 <= nx < M and tomato[ny][nx] == 0:
      tomato[ny][nx] = tomato[y][x] + 1
      queue.append((ny, nx))

cnt = 0
for i in tomato:
  for j in i:
    if j == 0:
      print(-1)
      exit(0)
  cnt = max(cnt, max(i))

print(cnt-1)
