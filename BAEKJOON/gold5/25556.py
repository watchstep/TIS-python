# 포스택
import sys;input=sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

stacks = [[] for _ in range(4)]

for n in A:
    is_append = False
    for stack in stacks:
        if not stack or stack[-1] < n:
            stack.append(n)
            is_append = True
            break
        
    if not is_append: # 어떤 stack에도 숫자 넣을 수 없을 경우
        print("NO")
        sys.exit(0)
print("YES")