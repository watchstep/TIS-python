# Four Squares
import math
import sys; input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]
dp[1] = 1

for i in range(2, n+1):
  min_cnt = 4
  # n보다 작거나 같은 제곱수 
  for j in range(int(math.sqrt(i)), 0, -1):
    min_cnt = min(min_cnt, dp[i-j**2]+1)
  dp[i] = min_cnt

print(dp[n])

# 다른 풀이
import sys; input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]
dp[1] = 1

for i in range(2, n+1):
  min_cnt = 4
  j = 1
  while (j**2) <= i:
    min_cnt = min(min_cnt, dp[i-(j**2)])
    j += 1
  dp[i] = min_cnt + 1 

print(dp[n])