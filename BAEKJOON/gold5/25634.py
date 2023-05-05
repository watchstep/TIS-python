# 전구 상태 뒤집기
import sys; input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = sum([x*y for x, y in zip(a, b)])

dp = []
tmp = 0
tmp2 = 0
for i in range(n):
  b2 = b[:]
  for j in range(i, n):
    b2[j] = 0 if b[j] else 1
    tmp2 += a[j] if b2[j] else 0
    dp.append() 
  
  tmp += a[i] if b[i] else 0

print(max(dp))

