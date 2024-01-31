# 겹치는 건 싫어
import sys;input=sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
start, end = 0, 0

cnt = [0 for _ in range(max(nums))]