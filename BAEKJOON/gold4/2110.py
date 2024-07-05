# 공유기 설치
import sys; input=sys.stdin.readline

n, c = map(int, input().split())

x_list = [int(input()) for _ in range(n)] # 집 위치 
x_list.sort() # 오름차순 정렬

start, end = 1, x_list[-1] - x_list[0] # 공유기 사이의 거리의 최솟값, 최댓값
res = []

while start <= end:
  cnt = 1
  mid = (start+end)//2 # 중간값 
  installed = x_list[0] # 공유기가 설치된 집 위치 왼쪽부터 시작
  
  for x in x_list:
    # 공유기 설치된 집 위치 + 중간값 (공유기 사이의 거리)이 집 위치보다 작거나 같으면,
    # 공유기 설치
    if installed + mid <= x:
      cnt += 1
      installed = x
  
  # 중간값 (공유기 사이의 거리)에 따라 설치된 공유기의 개수가
  # 설치할 공유기 개수 C보다 많거나 같으면
  if cnt >= c:
    start = mid + 1 # 공유기 사이의 거리 + 1
    res.append(mid)
  else:
    end = mid - 1 # 공유기 사이의 거리 -1
    
print(max(res))

