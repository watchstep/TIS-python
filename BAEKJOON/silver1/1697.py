# 숨바꼭질
import sys; input=sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
visited = [0 for _ in range(100001)]

def bfs(start):
  q = deque()
  q.append(start)
  
  while q:
    x = q.popleft()
    if x == k:
      return visited[x]
    nx_list = [x-1, x+1, x*2] # 이동위치
    
    for nx in nx_list:
      # 범위 벗어났을 때 
      if nx < 0 or nx > 100000:
        continue
      # 방문하지 않았을 때
      if visited[nx] == 0:
        visited[nx] = visited[x] + 1
        q.append(nx)

print(bfs(n))