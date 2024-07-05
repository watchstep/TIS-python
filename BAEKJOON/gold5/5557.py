# 1학년
import sys;input=sys.stdin.readline
from itertools import product

N = int(input())
nums = list(map(int, input().split()))
dp = [[0 for _ in range(21)] for _ in range(N - 1)] # 최댓값 20 (행 0 ~ 20, 열 N개)
dp[0][nums[0]] = 1 # 초깃값 (만들 수 있는 등식의 개수 저장)

for i in range(1, N - 1):
    for j in range(21):
        # 전에 계산했을 경우
        if dp[i - 1][j]:
            plus = j + nums[i]
            minus = j - nums[i]
            if plus <= 20:
                dp[i][plus] += dp[i - 1][j]
            
            if minus >= 0:
                dp[i][minus] += dp[i - 1][j]

print(dp[-1][nums[-1]])

# 시간초과
cnt = 0
for operators in product('+-', repeat=N-2):
    tmp = nums[0]
    for n, op in zip(nums[1:-1], operators):
        if tmp < 0 or tmp > 20:
            continue
        if op == "+":
            tmp += n
        else:
            tmp -= n
    
    if tmp == nums[-1]:
        cnt += 1

print(cnt)