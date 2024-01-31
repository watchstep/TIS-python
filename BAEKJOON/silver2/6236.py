# 용돈 관리
import sys; input=sys.stdin.readline

n, m = map(int, input().split())

use_money = []
for _ in range(n):
  use_money.append(int(input()))

def withdraw(a):
  cnt = 1
  curr_money = a
  for money in use_money:
    if curr_money < money:
      cnt += 1
      curr_money = a
      curr_money -= money
    else:
      curr_money -= money
  return cnt


def binary_search():
  start, end = max(use_money), sum(use_money)
  while start <= end:
    mid = (start+end)//2
    if withdraw(mid) > m:
      start = mid + 1
    else:
      end = mid - 1
  return start


print(binary_search())

# k 원 인출하고, 
# 모자르면 다시 집어넣고 k원 인출
# m번인출하고 싶음.
# 인출 금액 k를 최소화하기로 함.
