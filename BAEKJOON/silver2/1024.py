# 수열의 합
import sys; input = sys.stdin.readline

N, L = map(int, input().split())

for l in range(L, 101):
  seq_sum = l*(l+1) // 2
  seq_diff = N - seq_sum
  
  if seq_diff % l == 0:
    