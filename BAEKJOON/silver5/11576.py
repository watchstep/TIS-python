# Base Conversion
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
m = int(input())
digits = list(map(int, input().split())) # 높은 자릿수부터
digits.reverse() # 거꾸로 낮은 자릿수부터

num = 0
for i, x in enumerate(digits):
  num += x*a**i

res = []
while num >= b:
  digit = num % b
  num //= b
  res.append(digit)
else:
  res.append(num)

res.reverse()
print(*res)

# 2 * 17 + 16 = 50
# 50 % 8
# 50 // 8
# b진법 : base라 b