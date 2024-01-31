# 랭킹전 대기열
import sys;input=sys.stdin.readline

# 플레이어 수, 방 정원
p, m = map(int, input().split())

info = []
for _ in range(p):
  l, n = input().split()
  info.append((int(l), n))
  
