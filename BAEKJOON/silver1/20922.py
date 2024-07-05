# 겹치는 건 싫어
import sys;input=sys.stdin.readline
from collections import Counter

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 최장 연속 부분 수열 (투 포인터)
start, end = 0, 0
counter = Counter()
res = 0
while end < N:
    if counter[arr[end]] >= K:
        counter[arr[start]] -= 1
        start += 1
    else:
        counter[arr[end]] += 1
        end += 1
        
    res = max(res, end - start)

print(res)