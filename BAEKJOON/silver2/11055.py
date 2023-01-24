# 가장 큰 증가 부분 수열
import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

dp = seq[:]

for i in range(1, N):
  for j in range(i):
    if seq[i] > seq[j]:
      dp[i] = max(dp[i], dp[j]+seq[i])
      
print(max(dp))
