# 블랙잭
N, M = map(int, input().split())

nums = list(map(int, input().split()))

less_than = []
for i in range(N-2):
  for j in range(1, N-i):
    for e in range(1, N-i-j):
      sum = nums[i] + nums[i+j] + nums[i+j+e]
      if sum <= M:
        less_than.append(sum)
        
print(max(less_than))

# 다른 풀이
# 순열 combination
from itertools import combinations

N, M = map(int, input().split())

cards = list(map(int, input().split()))

res = 0

for combi in combinations(cards, 3):
  temp_sum = sum(combi)
  if temp_sum <= M:
    res = max(res, temp_sum)

print(res)
