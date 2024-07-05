# 회전 초밥 2531번 업그레이드 버전
import sys;input=sys.stdin.readline
from collections import Counter 

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
sushi.extend(sushi) # 원형 
start, end = 0, k
window = Counter() # 먹은 초밥 가록
window[c] += 1 # 쿠폰은 기본으로 먹기

# 초반 k개만큼 초밥 먹기
for i in sushi[start:end]:
    window[i] += 1
    
res = 0
while end < len(sushi):
    res = max(res, len(window))
    window[sushi[start]] -= 1 # 왼쪽 초밥 제거
    if not window[sushi[start]]: # 해당 초밥 없으면
        window.pop(sushi[start]) # window에서 없애기
    window[sushi[end]] += 1 # 오른쪽 초밥 추가
    start += 1
    end += 1
    
print(res)






        