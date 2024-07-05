# 진우의 민트초코우유
import sys;input=sys.stdin.readline

N, M, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
        
mincho = []
start_x, start_y = 0, 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            start_x, start_y = i, j
        elif graph[i][j] == 2:
            mincho.append((i, j))

res = 0
def dfs(x, y, hp, cnt):
    global res
    for mx, my in mincho:
        if graph[mx][my] == 2: # 아직 방문 안했으면
            dist = abs(x - mx) + abs(y - my)
            if hp >= dist:
                graph[mx][my] = -1 # 방문 처리
                dfs(mx, my, hp + H - dist, cnt + 1)
                graph[mx][my] = 2 # 우유 다시
    if hp >= abs(start_x - x) + abs(start_y - y):
        res = max(cnt, res)
            
dfs(start_x, start_y, M, 0)
print(res)