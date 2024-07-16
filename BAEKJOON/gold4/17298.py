# 오큰수
import sys;input=sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
NGE = [-1]*N
stack = []

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i]
    stack.append(i)

print(' '.join(map(str, NGE)))