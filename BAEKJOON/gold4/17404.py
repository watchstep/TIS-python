# RGB거리 2
import sys;input=sys.stdin.readline

N = int(input())
home = [list(map(int,  input().split())) for _ in range(N)]
INF = 1e9
res = INF

for i in range(3):
    # 첫 번째 집을 r, g, b 중 하나로 고정하고 시작
    dp = [[INF]*3 for _ in range(N)] # 초기화
    dp[0][i] = home[0][i] # 첫 번째 먼저 칠하고
    for j in range(1, N): # 두 번째 집은 그 다음 집과 다른 색으로
        dp[j][0] = home[j][0] + min(dp[j-1][1], dp[j-1][2]) # b
        dp[j][1] = home[j][1] + min(dp[j-1][0], dp[j-1][2]) # b
        dp[j][2] = home[j][2] + min(dp[j-1][0], dp[j-1][1]) # g
    for j in range(3):
        if i != j: # 첫 번째 집과 N번째 집 다른 색상일 때만
            res = min(res, dp[-1][j])
print(res)