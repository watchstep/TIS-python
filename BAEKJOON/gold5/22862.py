# 가장 긴 짝수 연속한 부분 수열 (large)
import sys;input=sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

end = 0
res = 0 # 가장 긴 짝수 수열 길이
tmp = 0 # 짝수 수열 길이 
cnt = 0 # 삭제 횟수
for start in range(N):
    while (end < N and cnt <= K):
        if arr[end] % 2 == 1:
            cnt += 1
        else:
            tmp += 1
        end += 1
        
        if not start and not end:
            res = tmp
            break
    if cnt == K + 1:
        res = max(tmp, res)
    if arr[start] % 2 == 1:
        cnt -= 1
    else:
        tmp -= 1

print(res)
            
# start, end = 0, 0
# for i in range(N):
#     if arr[i] % 2 == 1 and K > 0:
#         start += 1
#     elif arr[i] % 2 == 0 and K:
#         end -= 1
        