# 두 용액
import sys;input=sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
# 혼합 0에 가깝게
arr.sort()
start, end = 0, N
while start < end:
    mid = start + (end - start) // 2
    if abs( arr[mid] + arr[mid - 1]) > 1:


