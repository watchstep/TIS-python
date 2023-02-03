# 괄호의 값
import sys
input = sys.stdin.readline

ps = input().rstrip()

stk = []
res = 0
tmp = 1

for i in range(len(ps)):
  if ps[i] == '(':
    stk.append(2)
    tmp *= 2
  elif ps[i] == '[':
    stk.append(3)
    tmp *= 3
  elif ps[i] == ')':
    if not stk or stk[-1] != 2:
      res = 0
      break
    if ps[i-1] == '(':
      res += tmp
    stk.pop()
    tmp //= 2
  elif ps[i] == ']':
    if not stk or stk[-1] != 3:
      res = 0
      break
    if ps[i-1] == '[':
      res += tmp
    stk.pop()
    tmp //= 3
    
if stk:
  print(0)
else:
  print(res)
