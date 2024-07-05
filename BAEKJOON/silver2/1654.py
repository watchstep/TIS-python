# 랜선 자르기
import sys; input=sys.stdin.readline

k, n = map(int, input().split())

k_lines = []
for _ in range(k):
  k_lines.append(int(input()))

def fn(a):
  fn_list = list(map(lambda x: x // a, k_lines))
  cnt = sum(fn_list)
  return cnt

def binary_search(x):
  global k_lines
  start, end = 1, max(k_lines)+1
  while start <= end:
    mid = (start+end)//2
    if fn(mid) >= x:
      start = mid + 1
    else:
      end = mid - 1
  return start

print(binary_search(n)-1)
