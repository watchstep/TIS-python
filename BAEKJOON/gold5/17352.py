# 여러분의 다리가 되어 드리겠습니다!
import sys;input=sys.stdin.readline

N = int(input())
parents = [i for i in range(N + 1)]

def find(x): 
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
        
for _ in range(N-2):
    a, b = map(int, input().split())
    union(a, b)

res = []
for i in range(1, N + 1):
    if parents[i] == i: # 연결 안된 경우
        res.append(i)
print(*res)