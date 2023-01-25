# 후위 표기식2
import sys
input = sys.stdin.readline

N = int(input())
postfix = input().rstrip()

nums = []
for _ in range(N):
  nums.append(int(input()))
  
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
stack = []
for i in list(postfix):
  if i in alpha:
    stack.append(nums[ord(i)-ord('A')])
  else:
    b = stack.pop()
    a = stack.pop()
    if i == '*':
      stack.append(a*b)
    elif i == '/':
      stack.append(a/b)
    elif i == '+':
      stack.append(a+b)
    elif i == '-':
      stack.append(a-b)

print(f'{stack[0]:.2f}')

