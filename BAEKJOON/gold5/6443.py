# 애너그램
import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**5) # 25%  시간초과, 메모리초과..

def dfs_perm():
    global res
    if len(tmp) == m:
        res.append(''.join(tmp))
        return
    for i in range(m):
        if not visited[i]:
            visited[i] = True
            tmp.append(s[i])
            dfs_perm()
            visited[i] = False
            tmp.pop()
    
N = int(input())

for _ in range(N):
    s = list(input().rstrip())
    m = len(s)
    tmp = []
    res = []
    visited = [False]*m
    dfs_perm()
    res = set(res)
    print(*res, sep='\n')
    
# N과 M 시리즈
# from itertools import groupby list에서 중복된 것을 없애주는 것