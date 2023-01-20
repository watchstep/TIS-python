# 소수 최소 공배수
import sys
import math

N = int(sys.stdin.readline())
elems = set(list(map(int, sys.stdin.readline().split())))

def get_prime(e):
  for i in range(2, int(math.sqrt(e))+1):
    if e % i == 0:
      return False
  return True

primes = []
prime_lcd = 1
for e in elems:
  if get_prime(e):
    primes.append(e)
    prime_lcd *= e

if len(primes) > 0:
  print(prime_lcd)
else:
  print(-1)
