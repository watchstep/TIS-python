# 톱니바퀴
import sys;input=sys.stdin.readline

gears = []
for _ in range(4):
    gear = list(map(int, list(input().rstrip())))
    gears.append(gear)
    
K = int(input()) # 회전 횟수
for _ in range(K):
    n, d = map(int, input().split())
    n -= 1 # 파이썬은 0부터 index 시작하므로
    
def rotation():
    

# 반시계 
# (맨 앞에 있는 1이 뒤로)
# 시계
#  (맨 뒤에 있는 1이 앞으로)
# [0, 1, 2] / [0, 1, 2, 3, 4, 5, 6] / 

res = 0
if gear[0][0]:
    res += 1
elif gear[1][0]:
    res += 2
elif gear[2][0]:
    res += 4
elif gear[3][0]:
    res += 8

print(res)