# IF문 좀 대신 써줘
import sys; input=sys.stdin.readline

n, m = map(int, input().split()) # 칭호, 캐릭터 개수

name_list = []
cp_list = []

for _ in range(n):
  name, cp = input().split()
  name_list.append(name)
  cp_list.append(int(cp))

def binary_search(x):
  start, end = 0, len(cp_list)-1
  while start <= end:
    mid = (start+end)//2
    mid_cp = cp_list[mid]
    # 찾고자하는 값이 현재값보다 크면, 더 오른쪽으로
    if x > mid_cp:
      start = mid + 1
    else:
      end = mid - 1
  return name_list[end+1]

for _ in range(m):
  tmp = int(input())
  print(binary_search(tmp))

