import sys;input=sys.stdin.readline
from heapq import heappop, heappush

min_hq = []
max_hq = []
problem_dic = {}

N = int(input())
for _ in range(N):
	P, L = map(int, input().split())
	heappush(min_hq, (L, P)) # 난이도 낮은 순
	heappush(max_hq, (-L, -P)) # 난이도 높은 순
	problem_dic[P] = L


M = int(input())
for _ in range(M):
	cmd = input().split()
	if cmd[0] == 'add':
		P, L = map(int, cmd[1:])
		heappush(min_hq, (L, P)) # 난이도 낮은 순
		heappush(max_hq, (-L, -P)) # 난이도 높은 순
		problem_dic[P] = L

	elif cmd[0] == 'recommend':
		if cmd[1] == '1':
			while max_hq:
				L, P = heappop(max_hq)
				if -P in problem_dic and problem_dic[-P] == -L: # 삭제된 문제인지 여부 확인
					heappush(max_hq, (L, P)) # 삭제된 문제 아니므로 다시 넣음
					print(-P)
					break 
		else:
			while min_hq:
				L, P = heappop(min_hq)
				if P in problem_dic and problem_dic[P] == L:
					heappush(min_hq, (L, P))
					print(P)
					break

	elif cmd[0] == 'solved':
		P = int(cmd[1])
		if P in problem_dic:
			problem_dic.pop(P) # 힙에서는 제거 안 함