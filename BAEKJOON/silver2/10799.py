# 쇠막대기
import sys
input = sys.stdin.readline

ps = input().rstrip()

stk = []
cnt = 0
for i in range(len(ps)):
  if ps[i] == '(':
    stk.append(1)
  else:
    if ps[i-1] == '(':
      stk.pop()
      cnt += len(stk)
    else:
      stk.pop()
      cnt += 1

print(cnt)


