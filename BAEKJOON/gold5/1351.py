# 무한 수열
import sys;input=sys.stdin.readline
from collections import defaultdict

N, P, Q = map(int, input().split())
dic = defaultdict(int) # key: N, value: N // P + N // Q

def dfs(n):
    if n == 0:
        return 1
    if n in dic:
        return dic[n]
    dic[n] = dfs(n // P) + dfs(n // Q)
    return dic[n]

print(dfs(N))
