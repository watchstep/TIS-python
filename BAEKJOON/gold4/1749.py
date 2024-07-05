# 점수 따먹기
import sys;input=sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# Python으로 하면 시간초과
dp = [[0]*(M+1) for _ in range(N+1)]
res = int(-1e5)
for x in range(1, N+1):
    for y in range(1, M+1):
        dp[x][y] = dp[x-1][y] + dp[x][y-1] - dp[x-1][y-1] + arr[x-1][y-1]
        for i in range(1, x+1):
            for j in range(1, y+1):
                tmp = dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1]
                res = max(res, tmp)

print(res) 
# for x in range(1, N+1):
#     for y in range(1, M+1):
#         for i in range(1, x):
#             for j in range(1, y):
#                 tmp = dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1]
#                 res = max(res, tmp)
