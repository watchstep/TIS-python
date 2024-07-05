# 택배 배송
import sys; input = sys.stdin.readline
from heapq import heappush, heappop

n, m = map(int, input().split()) # 헛간 개수, 소들이 있는 길
INF = int(1e9) # 10억; 무한
distance = [INF]*(n+1)
graph = [[] for i in range(n+1)]

for _ in range(m):
  a, b, c = map(int, input().split()) # 헛간 a_i, 헛간 b_i, 소 마리수
  graph[a].append((b, c))
  graph[b].append((a, c))

def dijkstra(start):
  heap = []
  heappush(heap, (0, start)) # 시작 노드
  distance[start] = 0 # 시작 노드 -> 시작 노드 (자기 자신과의 거리는 0)
  while heap:
    dist, current_node = heappop(heap)
    # 우선순위 큐에서 꺼낸 거리가 이미 업데이트된 거리보다 큰 경우 (방문 처리) skip
    if distance[current_node] < dist:
      continue
    # 우선순위 큐에서 꺼낸 노드와 연결된 인접 노드 탐색
    for next_node, weight in graph[current_node]:
      # 더 작다면 다시 업데이트
      if (cost := dist + weight) < distance[next_node]:
        distance[next_node] = cost
        heappush(heap, (cost, next_node))
        
dijkstra(1)

print(distance[n])
        
