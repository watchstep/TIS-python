# 0 만들기
import sys; input=sys.stdin.readline
from itertools import product
  
cnt = int(input())

for _ in range(cnt):
  n = int(input())
  
  res = []
  # 조합 가능한 모든 경우의 연산자 리스트 
  for operators in product(['+', '-', ' '], repeat=n-1):
    num = 1
    exp = '1'
    for op in operators:
      num += 1
      exp += op + str(num)
    
    # eval 함수 사용해 문자열 그대로 계산한 결과가 0이면, res 리스트에 넣기  
    if not eval(exp.replace(' ', '')):
      res.append(exp)
  
  res.sort()
  print(*res, sep='\n')
  print()
  res = []