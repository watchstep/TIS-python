# 스타트링크
import sys; input = sys.stdin.readline
from collections import deque

f, s, g, u, d = map(int, input().split())

visited = [0]*(f+1) # 방문한 층수 저장

def bfs():
  q = deque([s])
  visited[s] = 1 # 방문 처리
  
  while q:
    p = q.popleft()
    
    if p == g:
      return visited[p] - 1
    
    # 위로, 아래로 (두 방향)
    for np in (p+u, p-d):
      if 0 < np <= f and not visited[np]: # 범위 안 넘어서고, 방문 안했으면
        q.append(np)
        visited[np] = visited[p] + 1
        
  return 'use the stairs'

print(bfs())