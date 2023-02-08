# 롤케이크
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
roll = list(map(int, input().split()))
roll.sort(reverse=True)

cnt = 0

a, b = divmod(20, 10)

for r in roll:
  if r == 10:
    cnt += 1
  elif r > 10 and M > 0:
    a, b = divmod(r, 10) # 몫 나머지
    s = a-1
    if b == 0:
      if s >= M:
        cnt += a
        M -= s
      else:
        cnt += M
        M = 1
    else:
      if a+1 >= M:
        cnt += a
        M -= s
      else:
        cnt += M
        M = 0

print(cnt)



