import sys;input=sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

res = -1
prefix =  [0]*(N + 1)
for i in range(1, N + 1):
	prefix[i] = prefix[i - 1] + arr[i - 1]

# 1. 벌통 오른쪽 끝
for i in range(1, N - 1):
	b1 = prefix[N] - arr[0] - arr[i]
	b2 = prefix[N] - prefix[i + 1]
	res = max(res, b1 + b2)

# 2. 벌통 왼쪽 시작
for i in range(1, N - 1):
	b1 = prefix[N] - arr[-1] - arr[i]
	b2 = prefix[i]
	res = max(res, b1 + b2)

# 3. 벌통 중간
for i in range(1, N - 1):
	b1 = prefix[i + 1] - arr[0]
	b2 = prefix[N - 1] - prefix[i] 
	res = max(res, b1 + b2)

print(res)