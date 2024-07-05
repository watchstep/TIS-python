# 바이러스
import sys;input=sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향

visited = [0]*(N+1)
def dfs(start_v):
    visited[start_v] = 1
    for next_v in graph[start_v]:
        if not visited[next_v]:
            dfs(next_v)

dfs(1)

print(sum(visited) - 1) # index를 0부터 시작했으니까

################################
import sys;input=sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향

visited = [False]*(N+1)
visited[1] = True
def bfs(start_v):
    q = deque([start_v])
    
    while q:
        curr = q.popleft()
        for next_v in graph[curr]:
            if not visited[next_v]:
                visited[next_v] = True
                q.append(next_v)
                
bfs(1)
print(sum(visited) - 1)