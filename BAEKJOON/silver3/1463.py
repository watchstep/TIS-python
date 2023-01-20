# 1로 만들기
import sys
input = sys.stdin.readline

N = int(input())
seq_3 = [0] + [0]*10**6
seq_2 = [0] + [0]*10**6

for i in range(1, N+1):
  if i