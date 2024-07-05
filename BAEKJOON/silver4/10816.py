# 숫자 카드 2
import sys; input=sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

card.sort() # 숫자 카드 정렬

# 위치를 알기 위해
def binary_search_lower(x):
  global card
  start, end = 0, len(card)
  while start < end:
    mid = (start+end)//2
    tmp = card[mid]
    if tmp < x:
      start = mid + 1
    else:
      end = mid
  return start


def binary_search_upper(x):
  global card
  start, end = 0, len(card)
  while start < end:
    mid = (start+end)//2
    tmp = card[mid]
    if tmp <= x:
      start = mid + 1
    else:
      end = mid
  return start

for n in nums:
  print(binary_search_upper(n) - binary_search_lower(n))

