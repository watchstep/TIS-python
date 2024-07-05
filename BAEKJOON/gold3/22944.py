# 죽음의 비
import sys;input=sys.stdin.readline
sys.setrecursionlimit(10000)

N, H, D = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 백트래킹, 종료 재귀...

is_u, is_e = False, False
d = 0
cnt = 0
def dfs(x, y):
    global cnt, is_u, d, is_e, H, D
    
    if (x < 0) or (x >= N) or (y < 0) or (y >= N):
        return 
    
    if graph[x][y] == 'E':
        is_e = True
        return
    
    if H <= 0:
        return 
    
    if graph[x][y] == 'U':
        is_u = True
        d = D
        
    if not visited[x][y]:
        cnt += 1
        visited[x][y] = -1
        if is_u and d > 0:
            d -= 1
        else:
            H -= 1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            dfs(nx, ny)
        
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'S':
            dfs(i, j)
            
print(cnt) if is_e else print(-1)