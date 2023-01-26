# 가장 긴 짝수 연속한 부분 수열 (small)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
seq = [int(i) for i in input().split()]

dp = [1]*N

for i in range(N):
  for j in range(i):
    if seq[i] > seq[j]:
      dp[i] = max(dp[i], dp[j]+seq[i])
      
print(max(dp))