# 스택
import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
  command = input().rstrip()
  
  if 'push' in command:
    num = command.split()[1]
    stack.append(int(num))
    
  elif 'pop' == command:
    if len(stack) < 1:
      print(-1)
    else:
      print(stack.pop())
      
  elif 'size' == command:
    print(len(stack))
    
  elif 'empty' == command:
    if len(stack) < 1:
      print(1)
    else:
      print(0)
      
  elif 'top' == command:
    if len(stack) < 1:
      print(-1)
    else:
      print(stack[-1])
