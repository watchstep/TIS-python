# 구간 합 구하기 4
# 누적 합 사용하기
import sys
N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0]
temp_sum = 0
for i in nums:
  temp_sum += i
  prefix_sum.append(temp_sum)


for _ in range(M):
  i, j = map(lambda x: int(x)-1, sys.stdin.readline().split())
  print(prefix_sum[j+1] - prefix_sum[i])

