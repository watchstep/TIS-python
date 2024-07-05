# 행복 유치원
import sys;input=sys.stdin.readline

N, K = map(int, input().split())
height = list(map(int, input().split()))
# 현재 상황에서 좋은 것만
# 1 3 5 6 10
# diff = 2 2 1 4
diff = []
for i in range(1, N):
    diff.append(height[i] - height[i-1])

diff.sort(reverse=True) # 내림차순 정렬 4 2 2 1
print(sum(diff[K - 1:])) # 2 + 1 = 3
    