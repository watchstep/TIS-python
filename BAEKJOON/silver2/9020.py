# 골드바흐의 추측
import sys
import math
input = sys.stdin.readline

T = int(input())

def is_prime(n):
  if n == 1:
    return False
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
      return False
  return True

for _ in range(T):
  tc = int(input())
  a, b =  tc//2, tc//2
  
  while a > 0:
    if is_prime(a) and is_prime(b):
      print(a, b)
      break
    a -= 1
    b += 1