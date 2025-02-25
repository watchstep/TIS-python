import sys;input=sys.stdin.readline
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False]*N for _ in range(N)]

def is_flower(x, y):
    cost = arr[x][y]
    positions = [(x, y)]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]: 
            return -1, []

        cost += arr[nx][ny]
        positions.append((nx, ny)) 

    return cost, positions


min_cost = 1e9
def backtracking(flower=0, cost=0):
	global min_cost
	if flower == 3:
		min_cost = min(min_cost, cost)
		return

	for i in range(1, N - 1): # 가장자리는 꽃 심을 수 없음
		for j in range(1, N - 1):
			tmp_cost, positions = is_flower(i, j)
			if tmp_cost != -1:

				# 방문 표시
				for x, y in positions:
					visited[x][y] = True

				backtracking(flower + 1, cost + tmp_cost)

				# 백트래킹 후 방문 해제 (꽃 심었다가 되돌리기)
				for x, y in positions:
					visited[x][y] = False

backtracking()
print(min_cost)