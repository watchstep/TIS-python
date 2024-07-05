# 백양로 브레이크
import sys;input=sys.stdin.readline

n, m = map(int, input().split())
graph = [[1e9]*(n+1) for _ in range(n+1)] # 최단 경로 담는 배열

for i in range(1, n+1):
    graph[i][i] = 0 # 자기자신
    
for _ in range(m):
    u, v, b = map(int, input().split())
    if b: # 일방
        graph[u][v] = 0
        graph[v][u] = 0
    else:
        graph[u][v] = 1
        graph[v][u] = 1

# 플로이드 워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

k = int(input())
for _ in range(k):
    s, e = map(int, input().split())
    