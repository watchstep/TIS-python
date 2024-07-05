# Z
import sys;input=sys.stdin.readline

N, r, c = map(int, input().split())
graph = [[0]*2**N for _ in range(2**N)] # 2^N x 2^N 배열
direction = [(1, 0), (-1, 1), (1, 0), (1, -1)] # 오른쪽 위, 왼쪽 아래, 오른쪽 아래, 왼쪽 위

res = 0
def dfs(x, y):
    global res
    if (x < 0) or (x >= 2**N) or (y < 0) or (y >= 2**N):
        return False
    if (x == r-1) and (y == c-1):
        return True
    if not graph[x][y]:
        graph[x][y] = -1 # 방문 처리
        res += 1
        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]
            dfs(nx, ny)

for i in range(2*N):
    for j in range(2*N):
        if dfs(i, j):
            print(res)
            

        