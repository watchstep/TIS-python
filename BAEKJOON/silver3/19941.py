# 햄버거 분배
import sys; input = sys.stdin.readline

n, k = map(int, input().split()) # 식탁 길이, 햄버거 선택 거리 
location = list(input()) # 사람, 햄버거 위치

res = 0

for i in range(n):
  if location[i] == "P":
    # 햄버거 선택 범위 
    for j in range(i-k, i+k+1):
      if 0 <= j < n and location[j] == "H":
        res += 1
        location[j] = "X"
        break

print(res)
        
