# 끝나지 않는 파티
import sys;input=sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# D_ab = min(D_ab, D_ak + D_kb)
def floyd_warshall():
    for k in range(N):
        for a in range(N):
            for b in range(N):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

floyd_warshall()

for _ in range(M):
    a, b, c = map(int, input().split())
    if graph[a - 1][b - 1] > c:
        print('Stay here')
    else:
        print('Enjoy other party')
