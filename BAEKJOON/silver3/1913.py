# 달팽이
import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

table = [[0]*N for _ in range(N)]

dx_y = [(0,1),(1,0),(0,-1),(-1,0)]
# 가운데 1
x, y = 0, 0
cnt = N**2
table[x][y] = cnt
d = 0
cnt -= 1

while cnt > 0:
  nx, ny = dx_y[t]