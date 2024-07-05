# 니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마 -1
import sys;input=sys.stdin.readline
from collections import Counter

N = int(input())
count = Counter()

for _ in range(N):
    te, tx = map(int, input().split())
    count[te] += 1
    count[tx] -= 1

max_cnt = 0
start, end = 0, 0
flag = False
mos_cnt = 0

for t in sorted(count.keys()):
    mos_cnt += count[t]
    if mos_cnt > max_cnt:
        max_cnt = mos_cnt
        start = t
        flag = True
    elif mos_cnt < max_cnt and flag:
        end = t
        flag = False

print(max_cnt)
print(start, end)