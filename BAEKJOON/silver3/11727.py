# 2xn 타일링 2
import sys;input=sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+1)]
dp[1] = 1

for i in range(2, n+1):
  if i == 2:
    dp[2] = 3
  else:
    dp[i] = dp[i-1] + 2*dp[i-2]
  
print(dp[n]%10007)