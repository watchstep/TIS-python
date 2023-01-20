# 1로 만들기
import sys
import math
input = sys.stdin.readline

N = int(input())
# index를 1부터 시작하도록 앞에 0 추가
seq = [0] + [0]*10**6

for i in range(2, N+1):
  seq[i] = seq[i-1] + 1
  if i % 2 == 0:
    seq[i] = min(seq[i], seq[i//2]+1)
  if i % 3 == 0:
    seq[i] = min(seq[i], seq[i//3]+1)
  
print(seq[N])

      
'''
1 : 0
2 : 1
3 : 1
4 : 2 (2*2)
5 : 3 (4+1)
6 : 2 (3*2)
7 : 3 (6+1)
8 : 3 (4*2)
9 : 2 (3*3)
10: 3 (9+1)
'''