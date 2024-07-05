# N과 M (10)
import sys;input=sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

tmp = []
visited = [False]*N

def back(start):
    if len(tmp) == M:
        print(*tmp)
        return
    check = 0
    for i in range(start, N):
        if not visited[i] and check != nums[i]:
            tmp.append(nums[i])
            check = nums[i]
            visited[i] = True
            back(i + 1)
            visited[i] = False
            tmp.pop()
            
back(0)