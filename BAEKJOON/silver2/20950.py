# 미술가 미미
import sys;input=sys.stdin.readline
from itertools import combinations

N = int(input())
paints = [list(map(int, input().split())) for _ in range(N)]
rb, gb, bb = map(int, input().split())

max_mix = N if N < 7 else 7

diff = 1e9
for i in range(2, max_mix + 1):
    for comb in combinations(paints, i):
        r = sum([p[0] for p in comb]) // i
        g = sum([p[1] for p in comb]) // i
        b = sum([p[2] for p in comb]) // i
        tmp = abs(r - rb) + abs(g - gb) + abs(b - bb)
        diff = min(diff, tmp)

print(diff)