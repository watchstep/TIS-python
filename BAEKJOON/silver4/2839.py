# 설탕 배달
N = int(input())

cnt = []

for bag_1 in range(0, 1667):
  for bag_2 in range(0, 1001):
    if 3*bag_1 + 5*bag_2 == N:
      total_bag = bag_1 + bag_2
      cnt.append(total_bag)

print(-1) if cnt == [] else print(min(cnt))

# 다른 풀이
N = int(input())

cnt = 0
while N >= 0:
  if N % 5 == 0: # 5의 배수이면
    cnt += N // 5 # 5로 나눌 때의 몫
    print(cnt)
    break
  
  N -= 3 # 5의 배수가 되도록 설탕 -3 봉지 + 1
  cnt += 1
  
else:
  print(-1) # 설탕이 음수일 때 (5, 3kg로 나눌 수 없음)
  
###### foe ~ else / while ~ else
for i in range(2, 8):
  for j in range(2, i):
    if i % j == 0:
      print(f'{i}는 {j}의 배수다')
      break
  else:
    print(f'{i}는 소수다')
    
n = 1
while n < 5:
  print(f'{n}은 5보다 작다')
  n += 1
else:
  print(f'{n}은 5 이상이므로 while문을 종료한다')