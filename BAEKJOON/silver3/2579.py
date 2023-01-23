# 계단 오르기
import sys
input = sys.stdin.readline

S = int(input())

score = [0]*300
dp = [0]*300

for i in range(S):
  score[i] = int(input())

dp[0] = score[0]
dp[1] = score[0] + score[1]
# 101 , 011
dp[2] = max(score[0]+score[2], score[1]+score[2])

for i in range(3, S):
  # 3계단 이전 합 + 011 , 2계단 이전 합 + 01
  dp[i] = max(dp[i-3]+ score[i-1] + score[i], dp[i-2] + score[i])

print(dp[S-1]) 
  

