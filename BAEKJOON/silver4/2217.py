# 로프
import sys
input = sys.stdin.readline

N = int(input())
k = [int(input()) for _ in range(N)]
# 최대 중량이 가벼운 순으로 정렬
k.sort()

cnt = len(k)
mw = k[0]*cnt

for i in range(1, len(k)):
  cnt -= 1
  temp = k[i]*cnt
  if temp >= mw:
    mw = temp

print(mw)
  
# 다른 풀이
import sys
input = sys.stdin.readline

N = int(input())
k = [int(input()) for _ in range(N)]

k.sort(reverse=True)
res = []

for i in range(N):
  res.append(k[i]*(i+1))
  
print(max(res))