# 별자리 만들기
import sys
import math
input = sys.stdin.readline

n = int(input())  
parents = [i for i in range(n)]
stars = []
edges = []
res = 0

for _ in range(n):
  x, y = map(float, input().split())
  stars.append((x, y))

def find(x):
  if parents[x] != x:
    parents[x] = find(parents[x])
  return parents[x]

def union(x, y):
  x = find(x)
  y = find(y)
  if x < y:
    parents[y] = x
  else:
    parents[x] = y

def dist(a, b):
  x_square = (a[0] - b[0])**2
  y_square = (a[1] - b[1])**2
  d = math.sqrt(x_square + y_square)
  return d

for i in range(n-1):
  for j in range(i+1, n):
    edges.append((dist(stars[i], stars[j]), i, j))
    
edges.sort()

for edge in edges:
  cost, x, y = edge
  if find(x) != find(y):
    union(x, y)
    res += cost

print(round(res, 2))


## 다른 풀이
import sys
import math
import heapq
input = sys.stdin.readline

n = int(input())  
stars = []
edges = []
res = 0

for _ in range(n):
  x, y = map(float, input().split())
  stars.append((x, y))

adj_edges = [[] for _ in range(n)]
visited = [0 for _ in range(n)]

# 별들 간 거리 계산
def dist(x1, y1, x2, y2):
	return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))

# 별 edge 쌍방 정보 저장
for i in range(n-1):
  for j in range(i+1, n):
    x1, y1 = stars[i]
    x2, y2 = stars[j]
    cost = dist(x1, y1, x2, y2)
    adj_edges[i].append([cost, j])
    adj_edges[j].append([cost, i])

def prim():
  res = 0
  q = []
  q.append([0, 1])
  
  while q:
    curr_cost, curr_node = heapq.heappop(q)
    
    if visited[curr_node] == 0:
      visited[curr_node] = 1
      res += curr_cost
      
      for next_cost, next_node in adj_edges[curr_node]:
        heapq.heappush(q, (next_cost, next_node))
	
  return res

print(prim())