# PPAP
import sys;input=sys.stdin.readline

S = input().rstrip()
stack = []

for s in S:
    stack.append(s)
    
    if len(stack) >= 4 and ''.join(stack[-4:]) == "PPAP":
        for _ in range(4):
            stack.pop()
        stack.append("P")

if ''.join(stack) == "P":
    print("PPAP")
else:
    print("NP")
