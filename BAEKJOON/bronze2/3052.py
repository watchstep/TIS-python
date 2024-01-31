# 나머지
import sys; input = sys.stdin.readline

res = []
for _ in range(10):
  num = int(input())
  na = num % 42
  res.append(na)

print(len(set(res)))