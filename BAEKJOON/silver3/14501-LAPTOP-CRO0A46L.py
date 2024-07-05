# 퇴사
import sys
input = sys.stdin.readline

N = int(input())
dp = [0]


for _ in range(N):
  T, P = map(int, input().split())
  