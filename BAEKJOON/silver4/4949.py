# 균형잡힌 세상
import sys;input=sys.stdin.readline

while True:
    s = input().rstrip()
    if s == ".":
        break
    
    stack = []
    for char in s:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(char)
                break
    
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(char)
                break

    if not stack:
        print("yes")
    else:
        print("no")
        