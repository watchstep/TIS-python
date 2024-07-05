# 표절
import sys;input=sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

def bin_search(idx):
    start, end = idx + 1, N - 1
    while (start <= end):
        mid = start + (end - start) // 2
        if arr[idx] >= 0.9 * arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return end - idx

res = 0
for i in range(N):
    res += bin_search(i)
print(res)
# 8 9 10 11 12 12 13
