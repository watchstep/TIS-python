import sys; input = sys.stdin.readline

N = int(input())

res = 1

for i in range(2, N+1):
  res *= i
  while True:
    if str(res)[-1] == '0':
      res //= 10
    else:
      break
  res %= 1000000000000

print(str(res)[-5:])

import math
a = math.factorial(1000000)

print(a)