# DFS와 BFS
import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
for i in graph:
  i.sort()

# 스택의 최상단 node 확인
# 최상단 node에 방문하지 않은 인접 노드가 있으면, 노드를 stack에 넣고, 방문 처리
# 방문하지 않은 인접 노드가 없으면, 스택에서 최상단 노드를 빼기

# 재귀 사용
def dfs(graph, start_node, visited=[False]*(N+1)):
  # 시작 노드
  visited[start_node] = True
  print(start_node, end=' ')
  # 방문해야하는 node가 남아있는 경우
  for node in graph[start_node]:
    if not visited[node]:
      dfs(graph, node, visited)


def bfs(graph, start_node, visited=[False]*(N+1)):
  visited[start_node] = True
  not_visited = deque([start_node])

  while not_visited:
    start_node = not_visited.popleft()
    print(start_node, end=' ')
    for i in graph[start_node]:
      if not visited[i]:
        not_visited.append(i)
        visited[i] = True

dfs(graph, V)
print()
bfs(graph, V)