# 행렬 곱셈 순서
import sys
input = sys.stdin.readline

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for diagonal in range(1, n): # dp[i][i] 자기 자신
  # 주대각선을 기준으로 상삼각행렬만 사용
  for i in range(n-diagonal): # 우측으로 한 칸씩 이동
    j = i + diagonal
    dp[i][j] = 2**32
    for k in range(i, j):
      dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + m[i][0]*m[k][1]*m[j][1])

print(dp[0][n-1])