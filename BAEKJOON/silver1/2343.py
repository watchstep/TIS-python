# 기타 레슨
import sys; input=sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

start, end = max(arr), sum(arr)
while start <= end:
    mid = start + (end - start) // 2
    
    tmp = 0
    cnt = 1
    for i in arr:
        if tmp + i > mid:
            cnt += 1
            tmp = 0
        tmp += i
            
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
        res = mid

print(res)