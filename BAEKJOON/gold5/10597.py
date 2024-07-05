# 순열장난
import sys;input=sys.stdin.readline

seq = input().rstrip()

# 11 9 + 2*2 = 13
L = len(seq)
if L < 10:
    N = L
else:
    N = 9 + (L - 9) // 2

