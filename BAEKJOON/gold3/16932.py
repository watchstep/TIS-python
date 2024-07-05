# 모양 만들기
import sys;input=sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int,  input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[-1]*M for _ in range(N)]

def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = group_num # 몇 번째 그룹인지 저장
    size = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] == -1 and arr[nx][ny] == 1:
                visited[nx][ny] = group_num
                q.append((nx, ny))
                size += 1
    return size

group_num = 0
group = [] # 1인 원소들의 그룹의 크기 저장
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == -1:
            group.append(bfs(i, j))
            group_num += 1

res = 0
for i in range(N):
    for j in range(M):
        if not arr[i][j]: # 0이면 상하좌우 보고
            check = set()
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if visited[nx][ny] not in check and arr[nx][ny] == 1:
                    check.add(visited[nx][ny])
            
            tmp = 1 # 0을 1로 바꿨다하고
            for c in check:
                tmp += group[c]
            
            res = max(res, tmp)    
            
print(res)
