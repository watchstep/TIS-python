# 조약돌 꺼내기
import sys

M = int(sys.stdin.readline()) # 조약돌 색상 개수
rock_colors = list(map(int, sys.stdin.readline().split())) # 색상별 조약돌 개수
K = int(sys.stdin.readline()) # 뽑는 조약돌 개수
N = sum(rock_colors) # 전체 조약돌 개수

def factorial(n):
  # 5! = 120
  if n == 1:
    res = 1
  else:
    res = factorial(n-1)*n
  return res


# combination n_C_k
def combi(n, k):
  res = factorial(n) / (factorial(n-k)*factorial(k))
  return res


def get_combi(n, k):
  res = 1
  for i in range(n-k+1, n+1):
    res = res*i
  return res

def get_prob(colors, k, n):
  # denominator => n_C_k
  de = get_combi(n, k)
  # numerator
  nu = 0
  for color in colors:
    if color >= k: # 같은 색상인 조약돌 개수가 뽑을 조약돌 개수 이상일 때
      nu += get_combi(color, k)
  res = nu / de
  return res

print(get_prob(rock_colors, K, N))

# 다른 풀이
import sys
import math

M = int(sys.stdin.readline()) # 조약돌 색상 개수
rock_colors = list(map(int, sys.stdin.readline().split())) # 색상별 조약돌 개수
K = int(sys.stdin.readline()) # 뽑는 조약돌 개수
N = sum(rock_colors) # 전체 조약돌 개수

de = math.comb(N, K)
nu = 0

for color in rock_colors:
  if color >= K:
    nu += math.comb(color, K)
    
print(nu / de)