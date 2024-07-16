# 좋은 단어
import sys;input=sys.stdin.readline

N = int(input())

res = 0
for _ in range(N):
    s = input().rstrip()
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    if not stack:
        res += 1
        
print(res)
    