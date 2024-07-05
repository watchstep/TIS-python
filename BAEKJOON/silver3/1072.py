# 게임
import sys;input=sys.stdin.readline

X, Y = map(int, input().split())

def get_z(a):
    return int((Y + a)*100/(X+ a))

start, end = 1, X
Z = get_z(0)
res = 0
if Z >= 99: # 승률이 99%일 때부터 바뀌지 않음
    print(-1)
else:
    while start <= end:
        mid = start + (end - start) // 2
        if get_z(mid) > Z:
            end = mid - 1 
            res = mid
        else:
            start = mid + 1
    print(res)


