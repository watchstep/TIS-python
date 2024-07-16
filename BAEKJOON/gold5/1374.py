# 강의실
import sys;input=sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: x[1]) # 강의 시작 시간으로 정렬

cnt = 0
hq = []

for l in lst:
    i, s, e = l
    while hq and hq[0] <= s: # 가장 빠른 종료 시간 < 시작 시간
        heappop(hq)
    
    heappush(hq, e)
    cnt = max(cnt, len(hq))
print(cnt)