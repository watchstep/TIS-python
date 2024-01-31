# N! mod P (1)
import sys
input = sys.stdin.readline

n, p = map(int, input().split()) # 양의 정수 N , N보다 큰 소수 P

# 파이썬에서는 "재귀"가 확실히 느림.
res = 1
for i in range(2, n+1):
  res *= i % p
  res %= p
  
print(res)

# 7 % 3 = 1
# 11 % 3 = 2
# 77 % 3 = 2 (1*2)
