# 뒤풀이
import sys;input=sys.stdin.readline

N, T = map(int, input().split())
conds = [list(map(int, input().split())) for _ in range(N)]
l_lst = [cond[0] for cond in conds]
r_lst = [cond[1] for cond in conds]

start, end = max(l_lst), max(r_lst)
res = -1
while start <= end:
    mid = start + (end - start) // 2 # S
    tmp = 0
    for l, r in conds:
        if l <= mid:
            tmp += min(mid, r)
    ########### 여기서 tmp 합을 어떻게 조정해줄지 레알로
    # 최소 다 나눠주고, 빼주면 그만큼 max 안에서 
    print(tmp, mid)
    if tmp > T:
        end = mid - 1
    elif tmp <= T:
        start = mid + 1
        res = mid
        
print(res)
            
# 2 - 5 / 4 - 10 / 1 - 3
# uppper bound 
# 디폴트 빼고 
# get_spare_drink
