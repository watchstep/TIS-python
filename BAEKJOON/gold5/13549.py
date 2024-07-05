# 숨바꼭질3
import sys;input=sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
visited = [0]*1000001
res = []
def bfs(start):
  q = deque([start])
  
  while q:
    x = q.popleft() 
    if x == k:
      return visited[x]
    nx_list = [x*2, x-1, x+1]
    for i in range(3):
      nx = nx_list[i]
      if nx < 0 or nx > 100000:
        continue
      if visited[nx] == 0:
        q.append(nx) 
        if i == 0: # 순간이동인 경우
          visited[nx] = visited[x]
        else:
          visited[nx] = visited[x] + 1
          
print(bfs(n))
