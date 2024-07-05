# 케빈 베이컨의 6단계 법칙
import sys; input=sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q = deque([start])
    
    while q:
        curr = q.popleft()
        for next in graph[curr]:
            if not visited[next]:
                visited[next] = visited[curr] + 1
                q.append(next)

min_kevin = 1e9
for i in range(1, N+1):
    visited = [0 for _ in range(N+1)]
    bfs(i)
    kevin = sum(visited)
    if min_kevin > kevin:
        min_kevin = kevin
        res = i

print(res)