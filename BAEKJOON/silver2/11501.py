# 주식
import sys;input=sys.stdin.readline

t = int(input())


for _ in range(t):
  n = int(input())
  p = list(map(int, input().split()))
  
  profit = 0
  max_p = 0
  for i in range(n-1, -1, -1):
    if p[i] > max_p:
      max_p = p[i]
    else:
      profit += max_p - p[i]
  else:
    print(profit)      
    