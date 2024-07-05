# N과 M (6)
import sys;input=sys.stdin.readline
from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

tmp = []
def dfs(start):
    if len(tmp) == M: # 백트래킹
        print(*tmp)
        return
    for i in range(start, N):
        tmp.append(nums[i]) 
        dfs(i + 1)
        tmp.pop()

dfs(0)

