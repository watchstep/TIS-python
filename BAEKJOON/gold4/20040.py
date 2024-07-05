# 사이클 게임
import sys;input=sys.stdin.readline

n, m = map(int, input().split())

parents = [i for i in range(n)] # 0 ~ n-1

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y:
        parents[y] = x
    elif x > y:
        parents[x] = y
    else: # cycle
        return True
    return False

for t in range(m):
    a, b = map(int, input().split())
    if union(a, b):
        print(t + 1)
        break
else:
    print(0)
