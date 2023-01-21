# 문자열 집합
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
include_list = []

for _ in range(N):
  include_list.append(input())
 
cnt = 0 
for _ in range(M):
  test = input()
  if test in include_list:
    cnt += 1
    
print(cnt)

# 다른 풀이 (set 사용함으로써 시간복잡도 줄임)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set([input() for _  in range(N)])
    
cnt = 0
for _ in range(M):
  t = input()
  if t in S:
    cnt += 1
    
print(cnt)