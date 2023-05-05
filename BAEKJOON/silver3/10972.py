# 다음 순열
import sys
input = sys.stdin.readline

N = int(input())
p = list(map(int, input().split()))

for i in range(N-1, 0, -1):
  # 뒤에 있는 숫자가 앞에 있는 숫자보다 큰 경우 ex) 1 2 3 4
  if p[i-1] < p[i]:
    for j in range(N-1, 0, -1):
      if p[i-1] < p[j]:
        # swap
        p[i-1], p[j] = p[j], p[i-1]
        p = p[:i] + sorted(p[i:])
        print(*p)
        exit()

print(-1)