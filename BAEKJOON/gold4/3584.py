# 가장 가까운 공통 조상
import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**6)

# 깊이 계산
def dfs(start_v, d):
    visited[start_v] = 1
    depth[start_v] = d
    for next_v in graph[start_v]:
        if not visited[next_v]:
            dfs(next_v, d + 1)
    

T = int(input())
for _ in range(T):
    N = int(input())
    graph = [[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    depth = [0 for _ in range(N+1)]
    parent = [0 for _ in range(N+1)]
    
    # 부모 노드 저장
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        parent[b] = a
    
    # lCA 구할 두 노드
    a, b = map(int, input().split())
    
    # 각 노드 깊이 계산
    for i in range(1, N+1):
        if not parent[i]:
            dfs(i, 0)
            break
        
    # 깊이 동일하도록
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 부모 노드 동일하도록
    while a != b:
        a = parent[a]
        b = parent[b]
    
    print(a)
    