# 점프
import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
  for j in range(N):
    if i == N-1 and j == N-1:
      break
    
    # board[i][j] : (i+1)행 (j+1)열
    x = j + board[i][j] # 오른쪽
    y = i + board[i][j] # 아래쪽
    
    if x < N:
      dp[i][x] += dp[i][j]
    if y < N:
      dp[y][j] += dp[i][j]
      
print(dp[N-1][N-1])
    
    