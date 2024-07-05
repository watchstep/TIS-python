# 물대기
import sys;input=sys.stdin.readline

N = int(input())
parents = [i for i in range(N+1)]
edges = []
for i in range(N):
    cost = int(input())
    edges.append((cost, 0, i+1))

graph = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(i):
        edges.append((graph[i][j], i+1, j+1))
        
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

edges.sort()
res = 0
for edge in edges:
    c, a, b = edge
    if find(a) != find(b):
        union(a, b)
        res += c 
print(res)

#########################
import sys;input=sys.stdin.readline
import heapq
from collections import defaultdict

N = int(input())

adj_edges = defaultdict(list)
for i in range(N):
    cost = int(input())
    adj_edges[0].append((cost, i + 1))

graph = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        adj_edges[i + 1].append((graph[i][j], j + 1))
        adj_edges[j + 1].append((graph[i][j], i + 1))

def prim():
    visited = [False]*(N+1)
    visited[0] = True # 시작 노드 방문 처리
    candidate = adj_edges[0]
    heapq.heapify(candidate)
    cnt = 0
    res = 0
    
    while candidate:
        if cnt == N:
            break
        cost, x = heapq.heappop(candidate)
        if not visited[x]:
            visited[x]= True
            cnt += 1
            res += cost
            
            for edge in adj_edges[x]:
                if not visited[edge[1]]:
                    heapq.heappush(candidate, edge)
    return res

print(prim())