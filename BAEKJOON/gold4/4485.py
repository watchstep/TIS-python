# 녹색 옷 입은 애가 젤다지?
import sys; input=sys.stdin.readline
from heapq import heappop, heappush

# 상, 하, 좌, 우 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dijkstra():
  heap = []
  heappush(heap, (cave[0][0], 0, 0))
  cost[0][0] = 0
  while heap:
    curr_cost, x, y = heappop(heap)
    if x == n-1 and y == n-1:
      return (f"Problem {idx}: {cost[x][y]}")
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx in range(n) and ny in range(n):
        if (new_cost := curr_cost + cave[nx][ny]) < cost[nx][ny]:
          cost[nx][ny] = new_cost
          heappush(heap, (new_cost, nx, ny))
      
idx = 1
while (n := int(input())) > 0:
  cost = [[sys.maxsize]*n for _ in range(n)] # 구해야하는 최소 비용
  cave = [list(map(int, input().split())) for _ in range(n)] # graph
  print(dijkstra())
  idx += 1
else:
  sys.exit()    