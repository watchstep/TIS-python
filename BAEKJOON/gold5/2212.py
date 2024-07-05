# 센서
import sys;input=sys.stdin.readline

N = int(input())
K = int(input())
lst = list(map(int, input().split()))
lst.sort()

diff = []
for i in range(N - 1):
    diff.append(lst[i + 1] - lst[i])
diff.sort()

print(sum(diff[:N - K])) # K개의 큰 가능영역 제거
