# 피로도
import sys
input = sys.stdin.readline

A, B, C, M = map(int, input().split())

hp = 0
w = 0

for h in range(24):
  if hp+A <= M:
    hp += A
    w += 1
  else:
    if hp-C > 0:
      hp -= C
    else:
      hp = 0

print(w*B)