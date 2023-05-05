# 여행 가자
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
# 자기 자신을 부모 노드로 설정
graph = [i for i in range(N)]

def find(x):
  if x != graph[x]:
    graph[x] = find(graph[x])
  return graph[x]

def union(x, y):
  x = find(x)
  y = find(y)
  if x < y:
    graph[y] = x
  else:
    graph[x] = y
    
for i in range(N):
  is_connect = list(map(int, input().split()))
  for j in range(N):
    if is_connect[j] == 1: # 두 도시 연결되어 있으면
      union(i, j) # 두 도시 union
  
path = list(map(lambda x:int(x)-1, input().split()))
start = graph[path[0]]
for i in range(M):
  if graph[path[i]] != start:
    print('NO')
    break
else:
  print('YES')