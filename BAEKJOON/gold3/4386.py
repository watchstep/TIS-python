# 별자리 만들기
import sys
import math
input = sys.stdin.readline

n = int(input())  
parents = [i for i in range(n+1)]
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