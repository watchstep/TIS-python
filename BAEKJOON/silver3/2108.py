# 통계학
import sys
N = int(sys.stdin.readline()) # 홀수

nums_dict = {}
nums = []
for _ in range(N):
  num = int(sys.stdin.readline().rstrip())
  nums.append(num)
  if num in nums_dict:
    nums_dict[num] += 1
  else:
    nums_dict[num] = 1
    
# 산술평균
nums.sort()
print(round(sum(nums) / N))

# 중앙값
print(nums[N//2])

# 최빈값
modes = []
max_cnt = max(nums_dict.values())

for num, cnt in nums_dict.items():
  if cnt == max_cnt:
    modes.append(num)

modes.sort()
print(modes[1]) if len(modes) > 1 else print(modes[0])

# 범위
print(max(nums) - min(nums))