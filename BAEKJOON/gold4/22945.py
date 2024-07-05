# 팀 빌딩
import sys;input=sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
res = 0
start, end = 0, N - 1

while start + 1 < end:
    tmp = (end - start - 1) * min(arr[start], arr[end])
    res = max(res, tmp)
    if arr[start] < arr[end]: # end - start는 줄어드므로, 능력치를 더 큰 쪽으로 이동
        start += 1
    else:
        end -= 1

print(res)