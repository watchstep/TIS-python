# 개구리 1
import sys;input=sys.stdin.readline

N, M = map(int, input().split())
interest  = [list(map(int, input().split())) for _ in range(N)]
flower = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))
    