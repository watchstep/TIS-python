# 옥상 정원 꾸미기
import sys;input=sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]

res = 0
stack = []
for l in lst:
    while stack:
        if stack[-1] <= l:
            stack.pop()
        else:
            break

    res += len(stack)
    stack.append(l)
        
print(res)

# [10] res = 0
# [10, 3] res = 1
# [10, 7] res = 1
# [10, 7, 4] 
# [10, 12]
# [10, 7, 12, 2]
