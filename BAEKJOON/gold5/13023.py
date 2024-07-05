# ABCDE
import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*N
flag = False
def dfs(a, depth=1):
    global flag
    visited[a] = True
    if depth == 5:
        flag = True
        return
    for i in graph[a]:
        if not visited[i]:
            dfs(i, depth + 1)
    visited[a] = False
        
for i in range(N):
    dfs(i)
    if flag:
        print(1)
        break
else:
    print(0)
    

