# 거울 설치
import sys;input=sys.stdin.readline
from collections import deque

n = int(input())
# 동서남북
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
house = [list(input().rstrip()) for _ in range(n)]
# 방문 처리 & 최소 거울 개수
visited = [[[-1]*4 for _ in range(n)] for _ in range(n)]
doors = []
for i in range(n):
    for j in range(n):
        if house[i][j] == '#':
            doors.append((i, j))
            
start_door_x, start_door_y = doors[0][0], doors[0][1]
end_door_x, end_door_y =  doors[1][0], doors[1][1]

# 3차원 BFS
def bfs(start_x, start_y):
    q = deque()
    # 시작 문 위치에서 시작할 방향 (동서남북) 
    for i in range(4):
        q.append((start_x, start_y, i))
        visited[start_x][start_y][i] = 0
    while q:
        x, y, direction = q.popleft()
        # 끝 문 위치일 때
        if x == end_door_x and y == end_door_y:
            print(visited[x][y][direction])
            break
        nx, ny = x + dx[direction], y + dy[direction]
        # 범위 벗어나거나 벽(*)일 때
        if nx < 0 or nx >= 0 or ny < 0 or ny >= n or house[nx][ny] == '*':
            continue
        # 거울 설치 가능하면
        if house[nx][ny] == '!':
            if not visited[nx][ny][direction]:
                q.append((nx, ny, direction))
                visited[nx][ny][direction] = visited[x][y][direction]
            if not visited[nx][ny][(direction + 1) % 4]:
                q.append((nx, ny, (direction + 1) % 4))
                visited[nx][ny][(direction + 1) % 4] = visited[x][y][direction] + 1
            if not visited[nx][ny][(direction - 1) % 4]:
                q.append((nx, ny, (direction - 1) % 4))
                visited[nx][ny][(direction - 1) % 4] = visited[x][y][direction] + 1
        elif house[nx][ny] == '#':
            return visited[x][y][direction]
    
print(bfs(start_door_x, start_door_y))