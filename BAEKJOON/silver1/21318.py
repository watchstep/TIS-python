# 피아노 체조
import sys
input = sys.stdin.readline

N = int(input())
M = list(map(int, input().split()))
Q = int(input())

diff_M = [0]*100000
for i in range(len(M)-1):
  if M[i] - M[i+1] > 0:
    diff_M[i] = diff_M[i-1] + 1
  else:
    diff_M[i] = diff_M[i-1]
    
for _ in range(Q):
  # index 0부터 시작하도록
  x, y = map(lambda x: int(x)-2, input().split())
  print(diff_M[y]-diff_M[x])
  