# 문제 추천 시스템 Version 1
import sys;input=sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
probs = [list(map(int, input().split())) for _ in range(N)]

M = int(input())
cmds = [list(input().split()) for _ in range(M)]

hq = []
for cmd in cmds:
    if cmd[0] == "add":
        pass
    elif cmd[1] == "recommend":
        pass
    else:
        hq.remove(int(cmd[1]))
