# 우주신과의 교감
import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())

# 우주신 좌표 저장
gods = []
for _ in range(n):
  x, y = map(int, input().split())
  gods.append((x, y))
  
# 우주신 좌표 간 거리 계산
def dist(x, y):
  return math.sqrt(math.pow(x[0] - y[0], 2) + math.pow(x[1] - y[1], 2))

# edge 정보 저장
edges = []
for i in range(n-1):
  for j in range(i+1, n):
    edges.append((dist(gods[i], gods[j]), i, j))

edges.sort() # 오름차순 정렬

parents = [i for i in range(n)]
def find(x):
  if x != parents[x]:
    parents[x] = find(parents[x])
  return parents[x]

def union(x, y):
  x = find(x)
  y = find(y)
  if x < y:
    parents[y] = x
  else:
    parents[x] = y

for _ in range(m):
  # index 0부터 시작하도록 
  g1, g2 = map(lambda x: int(x)-1, input().split())
  union(g1, g2)

res = 0
for edge in edges:
  dist, g1, g2 = edge
  if find(g1) != find(g2):
    union(g1, g2)
    res += dist
    
print(f'{res:.2f}')

