# 나무 자르기
import sys;input=sys.stdin.readline

N, M = map(int, input().split()) 
arr = list(map(int, input().split()))

start, end = 1, max(arr)
while start <= end:
    mid = start + (end - start) // 2
    tmp = 0
    for i in arr:
        if i > mid:
            tmp += i - mid
    if tmp >= M:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)

