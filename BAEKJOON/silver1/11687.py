# 팩토리얼 0의 개수
import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**7)

M = int(input().rstrip())

# 가장 끝 0의 개수 = 5의 배수 총 개수
def cnt_zero(n):
    return n // 5 + cnt_zero(n // 5) if n >= 5 else 0 

start, end = 1, M*5 # 상한을 꼭 최대치로 할 필요 X
res = -1
while start <= end:
    mid = start + (end - start) // 2
    cnt = cnt_zero(mid)
    
    if cnt < M:
        start = mid + 1
    elif cnt > M:
        end = mid - 1
    else:
        res = mid
        end = mid - 1 # 여기 안 넣어주면 시간초과 난다..조심..

print(res)
    