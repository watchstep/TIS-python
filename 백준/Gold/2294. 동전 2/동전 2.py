import sys;input=sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
dp = [1e9]*(k + 1) # x원을 만들기 위해 필요한 최소 동전의 개수
#  동전 순서나 어떤 동전을 사용했는지 알 필요 없으므로 1차원 dp 배열
dp[0] = 0

for coin in arr:
	for i in range(coin, k + 1):
		dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[-1] if dp[-1] != 1e9 else -1)