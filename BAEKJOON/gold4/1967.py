# 트리의 지름
import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(start_v, dist):
    for next_v, next_d in graph[start_v]:
        if visited[next_v] == -1:
            visited[next_v] = dist + next_d
            dfs(next_v, dist + next_d)
            
visited = [-1]*(n+1)
visited[1] = 0
dfs(1, 0) # 시작 정점에서

last_v = visited.index(max(visited))
visited = [-1]*(n+1)
visited[last_v] = 0
dfs(last_v, 0)

print(max(visited))
