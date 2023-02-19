# 집합의 표현
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
parents = [i for i in range(n+1)]

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
  cal, a, b = map(int, input().split())
  if cal == 0:
    union(a, b)
  else:
    if find(a) == find(b):
      print('YES')
    else:
      print('NO')
