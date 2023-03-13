# 퇴사
import sys
input = sys.stdin.readline

n = int(input())
consult = []

for _ in range(n):
  t, p = map(int, input().split())
  consult.append((t, p))
  
dp = [0 for _ in range(n+1)]

# 뒤에서부터 
for i in range(n-1, -1, -1):
  is_consult = consult[i][0] + i
  # 컨설팅 가능
  if is_consult <= n:
    dp[i] = max(dp[i+1], consult[i][1] + dp[is_consult])
  # 컨설팅 불가능
  else:
    dp[i] = dp[i+1]

print(max(dp))