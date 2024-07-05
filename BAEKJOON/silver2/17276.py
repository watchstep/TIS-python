# 배열 돌리기
import sys;input=sys.stdin.readline

T = int(input())

for _ in range(T):
    n, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    d //= 45
    
    if d == 1:
        pass
    elif d == 2:
        new_arr = list(map(list, list(zip(*arr))))
    elif d == 4:
        pass
    elif d == 5:
        pass
    elif d == 6:
        pass
    elif d == 7:
        pass
    elif d == 8:
        pass
    else:
        pass
    
    
# 45 90 135 180 225 270 315 360
arr = [list(map(int, input().split())) for _ in range(n)]
-45