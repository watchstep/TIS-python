# 회전초밥
import sys;input=sys.stdin.readline
from collections import defaultdict

n, d, k, c = map(int, input().split()) # 총 접시, 초밥, 연속해 먹은 접시, 쿠폰 번호
sushi = [int(input()) for _ in range(n)]
sushi.extend(sushi)

start, end = 0, 0
eat = defaultdict(int)

while end < k:
  eat[sushi[end]] += 1
  end += 1

eat[c] += 1 # 쿠폰
max_cnt = 0
while end < len(sushi):
  max_cnt = max(max_cnt, len(eat))
  eat[sushi[start]] -= 1
  if eat[sushi[start]] == 0:
    del eat[sushi[start]]
  
  eat[sushi[end]] += 1
  start += 1
  end += 1
  
print(max_cnt)  