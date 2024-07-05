# 뱀과 사다리 게임
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
dice = deque(range(1, 7))
xu = []
yv = []

for _ in range(N+M):
  a, b = map(int, input().split())
  xu.append(a)
  yv.append(b)

idx = 1
while idx < 100:
  d = dice.popleft()
  
  start_idx = 1
  while start_idx <=

1번칸 
1 ~ 6 애네를 queue에 나요
2 ~ 7번칸까지 한 번 굴려서 갈 수 있음
queue