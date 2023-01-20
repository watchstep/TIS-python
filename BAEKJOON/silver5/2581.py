# 소수
import math

M = int(input())
N = int(input())

def is_prime(n):
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
      return 0
  if n == 1:
    return 0
  return 1

primes = []

for i in range(M, N+1):
  if is_prime(i) == 1:
    primes.append(i)

if len(primes) > 0:
  print(sum(primes))
  print(min(primes))
else:
  print(-1)
