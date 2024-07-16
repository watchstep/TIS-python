# 오등큰수
import sys;input=sys.stdin.readline
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
F = Counter(A)
res = [-1]*N
stack = []

for i in range(N):
    while stack and F[A[stack[-1]]] < F[A[i]]:
        res[stack.pop()] = A[i]
    stack.append(i)

print(' '.join(map(str, res)))