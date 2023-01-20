# 모든 순열
import itertools

N = int(input())
for i in itertools.permutations(list(range(1, N+1)), N):
  for j in i:
    print(j, end=' ')
  print()  

# 직접 구현
N = int(input())