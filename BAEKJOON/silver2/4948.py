# 베르트랑 공준
# PyPy3로 시간초과 해결
import sys
import math
input = sys.stdin.readline

def is_prime(n):
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
      return 0
  return 1

n = int(input())

while n != 0:
  cnt = 0
  for i in range(n+1, 2*n+1):
    cnt += is_prime(i)
  print(cnt)
  n = int(input())

