# 시각
N, K = map(int, input().split())

# K가 포함되어 있는 시각 개수
cnt = 0

time = [0, 0, 0]

while True:
  check_list = []
  for i in time:
    if i < 10:
      check_list += [0, i]
    else:
      check_list += list(map(int, str(i)))
  if K in check_list:
    cnt += 1
     
  time[2] += 1
  if time[2] == 60:
    time[2] = 0
    time[1] += 1
  if time[1] == 60:
    time[1] = 0
    time[0] += 1
    
  if time == [N+1, 0, 0]:
    break

print(cnt)

# 다른 풀이
N, K = map(int, input().split())

cnt = 0
K = str(K)

for h in range(N+1):
  if h < 10:
    h = '0' + str(h)
  for s in range(60):
    if s < 10:
      s = '0' + str(s)
    for m in range(60):
      if m < 10:
        m = '0' + str(m)
      if K in str(h) + str(s) + str(m):
        cnt += 1

print(cnt)