# 괄호 제거
import sys;input=sys.stdin.readline
from itertools import combinations

exp = list(input().rstrip())

pairs = [] # 괄호 위치 저장
stack = []
for i in range(len(exp)):
    if exp[i] == '(':
        stack.append(i)
    elif exp[i] == ')':
        pairs.append((stack.pop(), i))

res = set()

for i in range(len(pairs)):
    for comb in combinations(pairs, i + 1):
        tmp = exp[:] 
        for start, end in comb:
            tmp[start] = "" # 괄호 제거
            tmp[end] = ""
        res.add(''.join(tmp))
        
print(*[i for i in sorted(list(res))], end='\n')

