# 트리의 부모 찾기
import sys
input = sys.stdin.readline
# 재귀 깊이 제한 (런타임 에러)
sys.setrecursionlimit(10**9)

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
  a, b = map(int, input().split())
  tree[a].append(b)
  tree[b].append(a)

parents = [0 for _ in range(N+1)]

def dfs(start_node):
  for node in tree[start_node]:
    if parents[node] == 0:
      parents[node] = start_node
      dfs(node)

dfs(1)

for i in range(2, N+1):
  print(parents[i])