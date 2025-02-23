# 2+1 세일
import sys;input=sys.stdin.readline

N = int(input())
C = [int(input()) for _ in range(N)]
C.sort(reverse=True)

res = sum(C)

for i in range(2, N, 3):
	res -= C[i]

print(res)