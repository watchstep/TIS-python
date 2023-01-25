# 스택 수열
# PyPy3 시간초과 해결
import sys
input = sys.stdin.readline

n = int(input())
seq = [int(input()) for _ in range(n)]

stk1 = []
stk2 = []
res = ''

s = 1
for i in seq:
  if i not in stk1:
    stk1.extend(list(range(s, i+1)))
    cnt = i+1-s
    res += '+\n'*(cnt if cnt > 0 else 0)
    s = i+1
    p = stk1.pop()
    res += '-\n'
    stk2.append(p)
  else:
    p = stk1.pop()
    res += '-\n'
    while p < i:
      p = stk1.pop()
      res += '-\n'
    else:
      stk2.append(p)

if stk2 == seq:
  print(res)
else:
  print('NO')

