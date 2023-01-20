# 소수 찾기
N = int(input())

n_lst = map(int, input().split())

# 소수 판별
def is_prime(n):
  for i in range(2, n):
    if n % i == 0:
      return 0
  return 1

total = 0

for n in n_lst:
  if n == 1:
    total -= 1
  total += is_prime(n)
  
print(total)