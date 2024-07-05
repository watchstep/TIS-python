# 수열의 합
import sys
input = sys.stdin.readline

N, L = map(int, input().split())

flag = False

for l in range(L, 101):
  start = N//l - l//2
  if l % 2 == 0:
    