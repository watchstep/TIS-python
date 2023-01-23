# 연속합
import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

for i in range(1, n):
  seq[i] = max(seq[i], seq[i-1]+seq[i])
  
print(max(seq))