# 딸기와 토마토
import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(N)]

garden_1 = []
for n in range(N):
  for m in range(M):
    if garden[n][m] == 1:
      garden_1.append((n, m))

# vertical
v = [g[0] for g in  garden_1]
# horizontal
h = [g[1] for g in  garden_1]
