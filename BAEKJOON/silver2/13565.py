# 침투
import sys; input=sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N = map(int, input().split())
fiber = []
for _ in range(M):
    fiber.append(list(map(int, input().strip())))
visited = [[False]*N for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
flag = False

def dfs(x, y):
    global flag
    if x < 0 or x >= M or y < 0 or y >= N:
        return
    if x == M-1:
        flag = True
        return
    if not fiber[x][y]:
        fiber[x][y] = -1 # 방문
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            dfs(nx, ny)
            
for i in range(N):
    if not fiber[0][i]:
        dfs(0, i)

if flag:
    print('YES')
else:
    print('NO')
