# 배열 복원하기
import sys; input=sys.stdin.readline

h, w, x, y = map(int, input().split())
# 배열 B
arr_b = [list(map(int, input().split())) for _ in range(h+x)]

for i in range(x, h):
  for j in range(y, w):
    arr_b[i][j] -= arr_b[i-x][j-y]

for i in range(h):
  print(*arr_b[i][:w])
    