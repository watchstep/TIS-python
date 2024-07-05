# 최대 힙
import sys;input=sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
heap = []

for _ in range(N):
    num = int(input())
    if num:
        heappush(heap, -num)
    else:
        largest = heappop(heap) if heap else 0
        print(-largest)
        

