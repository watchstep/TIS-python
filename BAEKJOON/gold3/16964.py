# DFS 스페셜 저지

import sys;input=sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
dfs_order = list(map(int, input().split()))

visited = [False for _ in range(N + 1)]
check = []
# 양방향 고려 (dfs, 수정)
def dfs(start_node):
    if visited[start_node]:
        return
    
    visited[start_node] = True
    check.append(start_node)
    
    for i in graph[start_node]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(1 if dfs_order == check else 0)

# 리스트 set으로 풀어보기