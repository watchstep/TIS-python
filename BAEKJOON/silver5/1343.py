# 폴리오미노
import sys
input = sys.stdin.readline

board = input().rstrip()
res = board.replace('XXXX', 'AAAA')
res = res.replace('XX', 'BB')

if 'X' in res:
  print(-1)
else:
  print(res)