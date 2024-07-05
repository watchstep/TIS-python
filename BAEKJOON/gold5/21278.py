# 호석이 두 마리 치킨
import sys;input=sys.stdin.readline

N, M = map(int, input().split())
graph = [[1e9]*(N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 자기 자신
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

# floyd warshall
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

####### 여기서부터 헷갈려 참고
res = 1e9
for i in range(1, N):
    for j in range(2, N + 1):
        tmp = 0
        for k in range(1, N + 1):
            tmp += min(graph[k][i], graph[k][j]) * 2 # 왜 *2를 하지..? 왕복
        if res > tmp:
            res = tmp
            buildings = [i, j]

print(*buildings, res)

# for i in range(N):
#   for j in range(i, N):
# 다익스트라
