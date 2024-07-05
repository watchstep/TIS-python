# 도시 건설
import sys;input=sys.stdin.readline

N, M = map(int, input().split())
parents = [i for i in range(N + 1)]
edges = []
total = 0
for i in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
    total += c

edges.sort() 

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

connect = 0
for edge in edges:
    c, a, b = edge
    if find(a) != find(b):
        union(a, b)
        connect += c
        
is_connect = 0
for i in range(1, N + 1):
    if parents[i] == i:
        is_connect += 1
        
if is_connect != 1:
    print(-1)
else:
    print(total - connect)
    # cnt = N - 1 break else - 1