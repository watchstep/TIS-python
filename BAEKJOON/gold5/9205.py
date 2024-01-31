# 맥주 마시면서 걸어가기
import sys; input=sys.stdin.readline
from collections import deque

t = int(input())

def get_dist(ax, ay, bx, by):
  return abs(ax-bx) + abs(ay-by)

def bfs():
  q = deque()
  q.append((hx, hy))
  while q:
    x, y = q.popleft()
    if get_dist(x, y, fx, fy) <= 1000:
      print('happy')
      return
    for i in range(n):
      if not visited[i]:
        nx, ny = graph[i]
        if get_dist(x, y, nx, ny) <= 1000:
          visited[i] = 1
          q.append((nx, ny))
  print('sad')
  return


for _ in range(t):
  n = int(input())
  hx, hy = map(int, input().split()) # 집
  graph = [tuple(map(int, input().split())) for _ in range(n)] # 편의점
  visited = [0 for _ in range(n+1)]
  fx, fy = map(int, input().split()) # 페스티벌
  bfs()
  