# 탑 (stack 사용해야 시간초과 x)
import sys;input=sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

res = [0]*N
stack = []
for i in range(N):
    while stack:
        if stack[-1][1] > lst[i]:
            res[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append((i, lst[i]))

print(*res)

# 4 -> 7 (4)
# 7 -> 9 (2)
# 5 -> 9 (2)
# 9 -> x (0)
# 6 -> x (0)