# 직각삼각형
import sys;input=sys.stdin.readline
from itertools import combinations

N = int(input())
arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

def get_dist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

cnt = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            l1 = get_dist(i[0], i[1])
            l2 = get_dist(i[1], i[2])
            l3 = get_dist(i[0], i[2])
            lst = [l1, l2, l3]
            lst.sort()
            if lst[-1] == (lst[0] + lst[1]):
                cnt += 1

print(cnt)   
# combination을 사용하면 시간초과
