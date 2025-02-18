import sys;input=sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
	x, y = map(int, input().split())
	graph[x].append(y)
	graph[y].append(x) # 촌수 계산하기 위해 부모-자식 간 연결 양방향

visited = [False]*(n + 1)
cnt = 0
def dfs(x, cnt=0):
	if x == b:
		return cnt

	visited[x] = True
	for nx in graph[x]:
		if not visited[nx]:
			tmp = dfs(nx, cnt + 1)
			if tmp != -1:
				return tmp
	return -1

print(dfs(a))