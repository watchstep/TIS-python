# 최소 스패닝 트리
import sys;input=sys.stdin.readline

V, E = map(int, input().split())
parent = [i for i in range(V+1)]
edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B)) # cost, A, B

edges.sort()        

def find(x):
    if parent[x] != x:
       parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

res = 0
for edge in edges:
    c, a, b = edge
    if find(a) != find(b):
        union(a, b)
        res += c 
print(res)