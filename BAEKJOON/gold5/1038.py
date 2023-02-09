# 감소하는 수
import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())

decrease_nums = []
# 제일 큰 감소하는 수 : 9876543210 10자릿수까지
for i in range(1, 11):
  # 0 ~ 9 숫자 조합
  for combi in combinations(range(0, 10), i):
    combi = list(combi)
    combi.sort(reverse=True)
    decrease_nums.append(int(''.join(map(str, combi))))

decrease_nums.sort()

try:
  print(decrease_nums[N])
except:
  print(-1)





