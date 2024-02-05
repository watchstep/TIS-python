# 문자열 잘라내기
import sys;input=sys.stdin.readline
from collections import Counter

R, C = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]
count = Counter()

cnt = 0
def binary_search_cnt():
    global cnt
    start, end  = 0, R - 1
    while (start <= end):
        mid = start + (end - start) // 2
        flag = True
        for c in range(C):
            tmp = ''
            for r in range(mid, R):
                tmp += arr[r][c]
            if not count[tmp]:
                count[tmp] += 1
            else:
                flag = False
                break
        if flag:
            cnt = mid
            start = mid + 1
        else:
            end = mid - 1

binary_search_cnt()
print(cnt)

                            