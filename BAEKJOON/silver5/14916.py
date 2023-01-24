# 거스름돈
import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
while n >= 0:
  if n % 5 == 0: # 5의 배수이면
    cnt += n // 5
    print(cnt)
    break
  
  n -= 2 # 5의 배수가 되도록 -2
  cnt += 1
  
else:
  print(-1) # 음수일 때 (5, 2의 조합으로 만들 수 없음)