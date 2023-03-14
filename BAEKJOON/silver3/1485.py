# 정사각형
import math
import sys; input = sys.stdin.readline

# 굳이 math.sqrt 안함
def get_dist(a, b):
  return math.pow(a[0]-b[0], 2) + math.pow(a[1]-b[1], 2)

def is_square(dots):
  d1 = get_dist(dots[0], dots[1])
  d2 = get_dist(dots[0], dots[2])
  d3 = get_dist(dots[0], dots[3])
  d4 = get_dist(dots[1], dots[2])
  d5 = get_dist(dots[1], dots[3])
  d6 = get_dist(dots[2], dots[3])
  # 정사각형 네 변 길이,두 대각선 길이
  dists = sorted([d1, d2, d3, d4, d5, d6])
  unique_dists = sorted(list(set(dists)))
  if len(unique_dists) == 2:
    ud1 = unique_dists[0] # 한 변 길이
    ud2 = unique_dists[1] # 대각선 길이
    if dists == [ud1]*4 + [ud2]*2 and ud1*2 == ud2:
      return 1
  return 0

t = int(input())

for _ in range(t):
  dots = []
  for _ in range(4):
    x, y = map(int, input().split())
    dots.append((x, y))
  print(is_square(dots))
  
