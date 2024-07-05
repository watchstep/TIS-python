# 인구 이동
import sys;input=sys.stdin.readline
from collections import deque

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
# L < 인구 차이 < R 국경선 열기
# 모두 열리면 
# 인접한 칸 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    q = deque()
    tmp = []
    q.append((a, b))
    tmp.append((a, b)) # tmp에 좌표값을 넣어주는 이유: 국경 공유하고 있는 나라들끼리 인구수 계산하기 위해
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny] == 1:
                continue
            if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                visited[nx][ny] = 1
                q.append((nx, ny))
                tmp.append((nx, ny))
    return tmp

res = 0
while True:
    visited = [[0]*(N) for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                country = bfs(i, j)
                if len(country) > 1:
                    flag = 1
                    new_pop = sum([graph[x][y] for x, y in country]) // len(country)
                    for x, y in country:
                        graph[x][y] = new_pop
                        
    if not flag:
        break

    res += 1

print(res)
                    
    