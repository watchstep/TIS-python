# 블로그

n, x = map(int, input().split()) # 블로그 일수, 방문 기간
visitors = list(map(int, input().split())) # 일별 방문자 수
dp = [0]*(n-x+1)
dp[0] = sum(visitors[:x])

for i in range(1, n-x+1):
  tmp = dp[i-1] - visitors[i-1] + visitors[i+x-1]
  dp[i] = tmp
  
res = max(dp)  
if not res:
  print('SAD')
else:
  print(res)
  print(dp.count(res))