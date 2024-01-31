# 하노이 탑 이동 순서
import sys;input=sys.stdin.readline

n = int(input())

cnt = 0
res = []
def hanoi(n, f, t, v):
  global cnt
  if n == 1:
    cnt += 1
    res.append((f, t))
  else:
    hanoi(n-1, f, v, t)
    res.append((f, t))
    hanoi(n-1, v, t, f)
    cnt += 1 # 실질적으로는 한 번 이동


hanoi(n, 1, 3, 2)
print(cnt)
for f, t in res:
  print(f, t)


# f -> t
# f -> v
# 마지막이 보조 막대
# v, t, f : v -> t 가는데 f를 보조막대