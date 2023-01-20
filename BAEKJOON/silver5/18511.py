# 큰 수 구성하기
import sys
N, K = map(int, sys.stdin.readline().split())
elems = list(sys.stdin.readline().split())

# N, N-1, ... 큰 수부터 시작
for i in range(N, 0, -1):
  # 543이면, ['5', '4', '3']으로 분리
  # 555이면 ['5']로 분리
  i_elems = list(set(str(i)))
  # 각 숫자가 K의 원소들 리스트에 있는지
  tf = list(map(lambda x : x in elems, i_elems))
  # [True, True, ...]
  digit = len(set(str(i)))
  if tf == [1]*digit:
    print(i)
    break
  

# 다른 풀이
import sys
from itertools import product
N, K = map(int, sys.stdin.readline().split())
elems = list(sys.stdin.readline().split())
elems.sort(reverse=True) # 큰 수부터 정렬

# K자릿수부터 1자릿수까지 K의 원소로만 만들 수 있는 수의 모든 가능한 순서 (중복 가능)
double_break = False
for i in range(len(str(N)), 0, -1):
  for j in product(elems, repeat=i):
    res = int(''.join(j))
    if res <= N:
      print(res)
      double_break = True
      break
  if double_break == True:
    break
