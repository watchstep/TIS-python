import sys; input=sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))
a.sort() # A 리스트 정렬


def binary_serach(x):
  global a
  start, end = 0, len(a)-1
  
  while start <= end:
    mid = (start+end) // 2
    tmp = a[mid]
    if tmp == x:
      return 1
    elif tmp < x:
      start = mid+1
    else:
      end = mid-1
  return 0
    

for n in nums:
  print(binary_serach(n))