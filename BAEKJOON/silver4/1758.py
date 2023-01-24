# 알바생 강호
import sys
input = sys.stdin.readline

N = int(input())
tip = [int(input()) for _ in range(N)]
# tip - rank (0부터 시작) 
tip.sort(reverse=True)

res = 0
for i in range(N):
  temp = tip[i]-i
  if temp > 0:
    res += temp

print(res)