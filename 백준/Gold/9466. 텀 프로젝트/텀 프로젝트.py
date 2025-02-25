# 텀 프로젝트 (DFS 사이클 판별)
import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node):
	global cnt
	visited[node] = True
	cycle.append(node) # 사이클 이루는 노드들은 팀 형성
	next_node = arr[node]

	if not visited[next_node]:
		dfs(next_node)
	elif next_node in cycle: # 이미 방문했고, 사이클에 있다면
		cycle_start_idx = cycle.index(next_node) # 사이클 시작 위치부터 한 팀
		cnt += len(cycle[cycle_start_idx:]) # 사이클 크기 (팀에 속한 학생 수)


T = int(input())
for _ in range(T):
	N = int(input())
	# 각 학생은 오직 1명의 학생만 선택 (edge 1개)
	arr = [0] + list(map(int, input().split())) 
	visited = [False]*(N + 1)
	cnt = 0
	for student in range(1, N + 1):
		if not visited[student]:
			cycle = []
			dfs(student)

	# 사이클 이루지 못한 노드 수
	print(N - cnt)