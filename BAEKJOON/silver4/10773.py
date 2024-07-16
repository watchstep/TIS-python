# 제로
import sys;input=sys.stdin.readline

K = int(input())
stack = []

for _ in range(K):
    i = int(input())
    if not i and stack:
        stack.pop()
    else:
        stack.append(i)
        
print(sum(stack))