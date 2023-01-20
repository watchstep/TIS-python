# 분해합
N = int(input())

cnt = 0
for i in range(1, N):
  desum = i + sum([int(i) for i in list(str(i))])
  if desum == N:
    cnt += 1
    print(i)
    break
  
if cnt == 0:
  print(0)
  
# 다른 풀이
N = int(input())

for i in range(1, N+1):
  desum = i + sum(map(int, str(i)))
  if desum == N:
    cnt += 1
    print(i)
    break
  if i == N:
    print(0)

de = sum(map(int, str(256)))
de