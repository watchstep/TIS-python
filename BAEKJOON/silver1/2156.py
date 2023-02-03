# 포도주 시식
import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]

dp = [0]*10000
dp[1:n+1] = wine[:]
# dp[:n+1] >>> [0, 6, 10, 13, 9, 8, 1]
dp[:n+1]

if n >= 2:
  dp[2] += dp[1]
  for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + dp[i], dp[i-3]+wine[i-2]+dp[i])
    
print(dp[n])
