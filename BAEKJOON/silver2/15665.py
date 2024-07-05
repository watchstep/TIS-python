# N과 M (11)
import sys;input=sys.stdin.readline

N, M = map(int, input().split())
nums = list(set(list(map(int, input().split())))) # 중복되는 수열을 피하기 위해 set

nums.sort()

tmp = []
def duplicate_perm():
    if len(tmp) == M:
        print(*tmp)
        return
    for n in nums:
        tmp.append(n)
        duplicate_perm()
        tmp.pop()
        
duplicate_perm()