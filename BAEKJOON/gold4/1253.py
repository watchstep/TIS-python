# 좋다
import sys;input=sys.stdin.readline

N = int(input())
nums = list(map(int, list(input().rstrip().split())))
nums.sort()

cnt = 0
for i in range(N):
    target = nums[i]
    tmp_lst = nums[:i] + nums[i+1:]
    start, end = 0, N - 2
    while start < end:
        tmp = tmp_lst[start] + tmp_lst[end]
        if tmp == target:
            cnt += 1
            break
        elif tmp < target:
            start += 1
        else:
            end -= 1

print(cnt)
    