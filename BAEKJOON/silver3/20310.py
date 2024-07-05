# 타노스
import sys;input=sys.stdin.readline

s = list(input())
cnt_0 = s.count('0') // 2
cnt_1 = s.count('1') // 2

for _ in range(cnt_0):
  s = s[::-1]
  s.remove('0')
  s = s[::-1]

for _ in range(cnt_1):
  s.remove('1') 

print(''.join(s))