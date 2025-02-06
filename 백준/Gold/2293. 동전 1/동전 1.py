import sys;input=sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

dp = [0]*(k + 1)
dp[0] = 1 # 0원을 만드는 경우의 수 1개

for coin in arr: 
	for i in range(coin, k + 1):
		if i >= coin:
			dp[i] += dp[i - coin]

print(dp[-1])