# 오목
import sys;input=sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(19)]

# → ↓ ↘ ↗
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

def check(x, y):
    for i in range(4):
        cnt = 1
        nx, ny = x + dx[i], y + dy[i]
        while (0 <= nx < 19) and (0 <= ny < 19) and (graph[nx][ny] == graph[x][y]):
            cnt += 1
            if cnt == 5:
                # next 육목
                nnx, nny = nx + dx[i], ny + dy[i]
                if (0 <= nnx < 19) and (0 <= nny < 19) and graph[nnx][nny] == graph[x][y]:
                    break
                # previous 육목
                px, py = x - dx[i], y - dy[i]
                if (0 <= px < 19) and (0 <= py < 19) and (graph[px][py] == graph[x][y]):
                    break
                print(graph[x][y])
                print(x + 1, y + 1)
                exit(0)
            # 업데이트    
            nx += dx[i]
            ny += dy[i]
            
            
for i in range(19):
    for j in range(19):
        if graph[i][j]:
            check(i, j)
else:
    print(0)