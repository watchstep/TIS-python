# 주몽
import sys;input=sys.stdin.readline

N = int(input())
M = int(input())
arr = list(map(int, list(input().split())))
arr.sort()

start, end = 0, N - 1
cnt = 0

while start < end:
	tmp = arr[start] + arr[end]
	if tmp == M:
		cnt += 1
		start += 1
		end -= 1
	elif tmp > M:
		end -= 1
	else:
		start += 1

print(cnt)