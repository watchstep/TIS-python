# 빗물
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
block_h = [*map(int, input().split())]

rain = 0
  

for i in range(1, W-1):
  left = max(block_h[:i])
  right = max(block_h[i+1:])
  
  tmp = min(left, right)
  
  # 
  if tmp > block_h[i]:
    rain += tmp - block_h[i]
    
print(rain)