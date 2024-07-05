# 사냥꾼
import sys;input=sys.stdin.readline

M, N, L = map(int, input().split())
gun_arr = list(map(int, input().split())) # 사대 좌표
arr = [list(map(int, input().split())) for _ in range(N)] # 동물 좌표

def bin_search(target):
    start, end = 0, M - 1
    while start < end:
        mid = start + (end - start) // 2
        mid_val = gun_arr[mid]
            
        if mid_val < target:
            start = mid + 1
        elif mid_val > target:
            end = mid - 1
        else:
            start = mid
    return start
        
gun_arr.sort()
cnt = 0
for x, y in arr:
    bin_idx = bin_search(x)
    
    dist = abs(x - gun_arr[bin_idx]) + y
    before_dist = abs(x - gun_arr[bin_idx - 1]) + y if bin_idx < M + 1 else 1e9
    next_dist = abs(x - gun_arr[bin_idx + 1]) + y if bin_idx < M - 1 else 1e9
    dist = min(dist, before_dist, next_dist)
    
    if dist <= L:
        cnt += 1
        
print(cnt)