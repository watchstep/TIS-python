# 전기가 부족해
import sys;input=sys.stdin.readline

N, M, K = map(int, input().split())
parents = [i for i in range(N + 1)]
edges = []

installed = list(map(int, input().split()))
for i in installed:
    parents[i] = installed[0]

for _ in range(M):
    u, v, w =  map(int, input().split())
    edges.append((w, u, v))

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

edges.sort()
res = 0
for edge in edges:
    c, a, b = edge
    if find(a) != find(b):
        union(a, b)
        res += c
print(res)
        