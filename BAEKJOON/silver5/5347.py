# LCM (최소공배수)
n = int(input())


# LCD (최대공약수) 구하는 함수
def get_lcd(a, b):
  cds = []
  for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i ==0:
      cds.append(i)
  return max(cds)

# LCM 구하는 함수 
def get_lcm(a, b):
  lcd = get_lcd(a, b)
  lcm = a * (b//lcd)
  return lcm

for _ in range(n):
  a, b = map(int, input().split())
  print(get_lcm(a, b))

# 다른 풀이 1
a, b = 10, 12

def gcd(a, b):
  while(b):
    a, b = b, a%b
  return a

def lcd(a, b):
  res = (a * b) // gcd(a, b)
  return res

gcd(a, b)
lcd(a, b)

# 다른 풀이 2
import math
math.lcm(15, 21)