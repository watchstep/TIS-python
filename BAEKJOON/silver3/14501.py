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

# 다른 풀이 (DFS 알고리즘)
import sys
input = sys.stdin.readline

n = int(input())
consult = []

for _ in range(n):
  t, p = map(int, input().split())
  consult.append((t, p))
  
max_profit = 0

def dfs(day, profit):
  global max_profit
  # 퇴사일일 때
  if day == n:
    max_profit = max(max_profit, profit)
    return
  
  t = consult[day][0] # 컨설팅 걸리는 일수
  p = consult[day][1] # 컨설팅 수입
  
  # 컨설팅 가능할 경우
  if t + day <= n:
    dfs(t+day, profit+p)
  # 컨설팅 불가능할 경우
  dfs(day+1, profit)

# 시작일부터 순차적으로 방문
for day in range(n):
  dfs(day, 0)
  
print(max_profit)