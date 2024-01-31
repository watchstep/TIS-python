# 집합
import sys;input=sys.stdin.readline

m = int(input()) # 연산수

s = set()
def calculate(x, y=None):
  global s
  if x == 'add':
    s.add(y)
  elif x == 'remove':
    s.discard(y)
  elif x == 'check':
    print(1 if y in s else 0)
  elif x == 'toggle':
    s.remove(y) if y in s else s.add(y)
  elif x == 'all':
    s = set(range(1, 21))
  else:
    s = set()
  
for _ in range(m):
  cal = input().split()
  if len(cal) > 1:
    calculate(cal[0], int(cal[1]))
  else:
    calculate(cal[0])
