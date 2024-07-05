# 징검다리 건너기 (large)
import sys; input=sys.stdin.readline

N = int(input())
power = list(map(int, input().split()))
dp = [0] + [1e9]*(N-1)

for i in range(1, N):
    for j in range(0, i):
        tmp = max((i - j) * (1 + abs(power[i] - power[j])), dp[j])
        dp[i] = min(dp[i], tmp)

print(dp[-1])
       