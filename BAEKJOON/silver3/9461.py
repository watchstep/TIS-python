# 파도반 수열
import sys
input = sys.stdin.readline

T = int(input())
# 시작 인덱스를 1로 맞추기 위해 앞에 0 추가
seq = [0, 1, 1, 1, 2, 2] + [0] * 95

for i in range(6, 101):
  seq[i] = seq[i-2] + seq[i-3]
  
for _ in range(T):
  N = int(input())
  print(seq[N])


# 1+2
# 2 + 2
# 2 + 3
# 3 + 4