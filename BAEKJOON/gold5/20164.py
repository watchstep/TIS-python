# 홀수 홀릭 호석
import sys;input=sys.stdin.readline
from itertools import combinations

N = input().strip()

def odd_cnt(n):
    cnt = 0
    for i in n:
        if int(i) % 2 == 1:
            cnt +=1
    return cnt

res = [1e9, 0]
def odd_holic(n, cnt=0):
    global res
    cnt += odd_cnt(n)
    if len(n) > 2:
        partition = range(1, len(n))
        for l, r in combinations(partition, 2):
            start, middle, end = n[:l], n[l:r], n[r:]
            tmp = str(int(start) + int(middle) + int(end))
            odd_holic(tmp, cnt)
    elif len(n) == 2:
        tmp = str(int(n[0]) + int(n[1]))
        odd_holic(tmp, cnt)
    else:
        res = [min(cnt, res[0]), max(cnt, res[1])]
        return

odd_holic(N)
print(*res)
    
    
    
    
