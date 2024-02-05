#노드사이의 거리
import sys;input=sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def bfs(start, end):
    q = deque()
    q.append((start, 0)) # 시작 노드, 거리
    
    visited = [False]*(N+1)
    visited[start] = True # 방문 처리
    
    while q:
        curr_node, curr_dist = q.popleft()
        
        if curr_node == end:
            return curr_dist
        
        for next_node, next_dist in graph[curr_node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append((next_node, curr_dist + next_dist))

for _ in range(M):
    a, b = map(int, input().split())
    print(bfs(a, b))