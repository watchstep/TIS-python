# 최소 힙
import sys; input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input()) # 연산 개수
heap = []

for _ in range(n):
  x = int(input())
  if not x:
    print(heappop(heap) if len(heap) else 0)
  else:
    heappush(heap, x)