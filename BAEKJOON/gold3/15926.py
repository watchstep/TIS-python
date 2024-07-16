# 현욱은 괄호왕이야!!
import sys;input=sys.stdin.readline

n = int(input())
s = input().rstrip()

# 괄호 인덱스 저장
stack = []
res = 0
last_invalid = -1
for i in range(n):
    if s[i] == ")":
        if not stack: # 스택이 비어있으면
            last_invalid = i # 현재 인덱스를 마지막 유효하지 않은 괄호로 기억
        else:
            stack.pop() 
            if not stack: # 스택이 비어있다면
                res = max(res, i - last_invalid) 
            else:
                res = max(res, i - stack[-1])
    else:
        stack.append(i)
    
print(res)