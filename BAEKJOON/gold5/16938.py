# 캠프 준비
import sys;input=sys.stdin.readline
from itertools import combinations

N, L, R, X = map(int, input().split())
A_lst = list(map(int, input().split()))

cnt = 0
for i in range(1, N+1):
    for j in combinations(A_lst, i):
        score = sum(j)
        diff = max(j) - min(j)
        if score >= L and score <= R and diff >= X:
            cnt +=1

print(cnt)