# 플로이드
import sys
input = sys.stdin.readline

n = int(input()) # 노드
m = int(input()) # 간선
INF=int(1e9)
graph = [[INF]*n for _ in range(n)]

# 자기 자신으로 가면 0
for i in range(n):
  for j in range(n):
    if i == j:
      graph[i][j] = 0
      
for _ in range(m):
  # 버스 index 1부터 시작
  a, b, c = map(int, input().split())
  graph[a-1][b-1] = min(c, graph[a-1][b-1])

# 플로이드 워셜 알고리즘
for i in range(n):
  for j in range(n):
    for k in range(n):
      graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
      
# INF -> 0
for i in range(n):
  for j in range(n):
    if graph[i][j] == INF:
      graph[i][j] = 0

for i in graph:
  print(' '.join([str(x) for x in i]))
