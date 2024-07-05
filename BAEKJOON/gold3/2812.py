# 크게 만들기
import sys;input=sys.stdin.readline

N, K = map(int, input().split())
num = input().rstrip()

stack = []
for n in num:
    while stack and K > 0 and (stack[-1] < n):
        stack.pop()
        K -= 1
    stack.append(n)

print(''.join(stack[:N - K])) # K가 0 이상인 경우
    
