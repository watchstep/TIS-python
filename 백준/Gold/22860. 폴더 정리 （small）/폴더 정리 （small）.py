import sys;input=sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())
tree = defaultdict(lambda: {'folders': {}, 'files': set()})

for _ in range(N + M):
	P, F, C = input().split()
	if int(C):
		tree[P]['folders'][F] = {'folders': {}, 'files': set()}
	else:
		tree[P]['files'].add(F)

def dfs(folder):

	stack = [folder]
	files = []

	while stack:
		x = stack.pop()
		if tree[x]['files']:
			files.extend(list(tree[x]['files']))
		stack.extend(tree[x]['folders'])
	return files


Q = int(input())
for _ in range(Q):
	query = input().rstrip().split('/')
	res = dfs(query[-1])
	print(len(set(res)), len(res))