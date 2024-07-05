# 나무 탈출
import sys;input=sys.stdin.readline
from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(N + 1)
res = 0

def bfs():
    global res
    q = deque()
    q.append((0, 1)) # degree, start_node
    visited[1] = True
    
    while q:
        degree, node = q.popleft()
        is_leaf = True
        for next_node in graph[node]:
            if not visited[next_node]:
                is_leaf = False
                visited[next_node] = True
                q.append((degree + 1, next_node))
                
        if is_leaf:
            res += degree
bfs()

print("No") if res % 2 == 0 else print("Yes")
