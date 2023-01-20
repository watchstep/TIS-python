# 수 정렬하기2
import sys
N = int(input())

nums = []
for _ in range(N):
  num = int(sys.stdin.readline())
  nums.append(num)

nums.sort()

for n in nums:
  print(n)