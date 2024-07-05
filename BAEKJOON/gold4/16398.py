# 행성 연결
import sys;input=sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
parents = [i for i in range(N)] # parents 자기 자신으로 초기화
edges = []

# 대각선 기준 대칭, i+1 ~ N
for i in range(N):
    for j in range(i + 1, N):
        edges.append((graph[i][j], i, j)) # cost, i, j
        
edges.sort() # cost 낮은 순으로 정렬

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
   
res = 0     
for edge in edges:
    cost, i, j = edge
    # find -> 부모 노드 다르면 사이클 없으면 union -> 최소 신장 트리
    if find(i) != find(j):
        union(i, j) # 연결
        res += cost
        
print(res)
