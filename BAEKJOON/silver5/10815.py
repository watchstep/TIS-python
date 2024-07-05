# 숫자 카드
import sys;input=sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

arr.sort()
def bin_search(target):
    start, end = 0, N - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

res = [bin_search(i) for i in arr2]
print(*res)