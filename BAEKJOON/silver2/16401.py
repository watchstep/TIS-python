# 과자 나눠주기
import sys; input=sys.stdin.readline

M, N = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, N
while start <= end:
    mid = start + (end - start) // 2
    if arr[mid] 