import sys;input=sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
hq = []
for _ in range(N):
	bundle = int(input())
	heappush(hq, bundle) # 카드 묶음을 우선순위 큐에 넣기

cnt = 0
while len(hq) > 1: # 묶음이 하나만 남을 때까지 반복
	a = heappop(hq) # 가장 작은 두 묶음을 꺼내기
	b = heappop(hq)
	combined = a + b # 합친 묶음
	heappush(hq, combined)
	cnt += combined # 매 단계마다 두 묶음 합친 횟수 누적

print(cnt)