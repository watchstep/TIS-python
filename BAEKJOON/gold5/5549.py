# 행성 탐사
import sys;input=sys.stdin.readline

M, N = map(int, input().split()) # 세로 M 가로 N
K = int(input().rstrip())
map_arr = [list(input().rstrip()) for _ in range(M)]
info_arr = [list(map(int, input().split())) for _ in range(K)]

dp = [[[0]*3]*(N+1) for _ in range(M+1)] # 개수 누적합 (J, 0, I)
for i in range(1, M+1):
    for j in range(1, N+1):
        dp[i][j] = [a + b - c for a, b, c in zip(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])]
        
        if map_arr[i-1][j-1] == 'J':
            dp[i][j][0] += 1
        elif map_arr[i-1][j-1] == 'O':
            dp[i][j][1] += 1
        else:
            dp[i][j][2] += 1
            
for a, b, c, d in info_arr:
    res = [i - j - k + z for i, j, k, z in zip(dp[c][d], dp[c][b-1], dp[a-1][d], dp[a-1][b-1])]
    print(*res)
