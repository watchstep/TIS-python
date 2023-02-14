# 램프
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

# 램프 상태 (N*M)
status = []
for _ in range(N):
  row = tuple(int(i) for i in list(input().rstrip()))
  status.append(row)
  
K = int(input())

unique_status = list(set([i for i in status]))

duplicate_cnt = []
for row in unique_status:
  duplicate_cnt.append(status.count(row))

max_cnt = 0
for row, cnt in zip(unique_status, duplicate_cnt):
  off_cnt = row.count(0)
  if off_cnt <= K and off_cnt%2 == K%2: # 해당 행 전구 모두 킬 수 있는 조건
    max_cnt = max(cnt, max_cnt)
print(max_cnt)


# 다른 풀이
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

status = []
for _ in range(N):
  status.append(input().rstrip())
  
K = int(input())

res = 0
for k in range(K, -1, -2):
  tmp = []
  for s in status:
    if s.count('0') == k:
      tmp.append(s)
  if len(tmp) != 0:
    tmp_cnt = max([tmp.count(x) for x in tmp])
    res = max(res, tmp_cnt)
    
print(res)
