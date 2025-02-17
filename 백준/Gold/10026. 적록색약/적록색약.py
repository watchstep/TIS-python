import sys;input=sys.stdin.readline
from collections import deque

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]

visited = [[False]*N for _ in range(N)]
visited_blind = [[False]*N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(sx, sy, is_blind):
	q = deque([(sx, sy)])
	visited[sx][sy] = True
	
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			if nx < 0 or nx >= N or ny < 0 or ny >= N:
				continue
			if is_blind:
				if not visited_blind[nx][ny]:
					if (arr[nx][ny] == arr[x][y]) or (arr[x][y] in 'RG' and arr[nx][ny] in 'RG'):
						visited_blind[nx][ny] = True
						q.append((nx, ny))
			else:
				if not visited[nx][ny] and arr[nx][ny] == arr[x][y]:
					visited[nx][ny] = True
					q.append((nx, ny))


cnt, blind_cnt = 0, 0

for i in range(N):
	for j in range(N):
		if not visited[i][j]:
			bfs(i, j, False) # bfs 실행 -> 한 구역 탐색 완료
			cnt += 1
		if not visited_blind[i][j]:
			bfs(i, j, True)
			blind_cnt += 1

print(cnt, blind_cnt)