# 우유 도시
import sys;input=sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [1, 0] # 동쪽, 남쪽
dy = [0, 1]

milk = 0
def dfs(x, y): # 재귀 구현
    global milk
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if graph[x][y] == milk: # 마셔야하는 종류의 유유면
        graph[x][y] = -1 # 방문 처리
        if milk == 2:
            milk = 0
        else:
            milk += 1
        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            dfs(nx, ny)
        return True
    
cnt = 0
for i in range(N):
    for j in range(N):
        if dfs(i, j):
            cnt += 1

print(cnt)
            
            
                