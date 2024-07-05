# 조 짜기
import sys;input=sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
# 조를 몇 개 짜야하는지
dp = [0]*(N + 1) # 조가 1개이면 점수합 0

for i in range(2, N + 1):
    for j in range(1, i + 1):
        tmp = arr[i - j:i]
        print(tmp)
        diff = max(tmp) - min(tmp)
        dp[i] = max(dp[i], dp[i - j] + diff)
        
print(dp[-1])
    
# 2 5 7 1 / 3 4 8 6 / 9 3
# 2 / 5 7 1 3 / 4 8 6 9 / 3

# for i in range(2, N + 1):
#     tmp = 0
#     for k in range(0, N, i):
#         ttmp = 0
#         for j in range(N):
#             print(arr[j:i + k + j])
#             high = max(arr[j:i + k + j])
#             low = min(arr[j:i + k + j])
#             ttmp += (high - low)
#         tmp = max(tmp, ttmp)
#     dp[i] = max(dp[i - 1], tmp)