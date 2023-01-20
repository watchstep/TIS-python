# 수학은 비대면강의입니다
a, b, c, d, e, f = map(int, input().split())

x = (f*b - c*e) // (d*b - a*e)
y = (c - a*x) // b

print(x, y)

# 다른 풀이
a, b, c, d, e, f = map(int, input().split())

for i in range(-999, 1000):
  for j in range(-999, 1000):
    if (a*i) + (b*j) == c and (d*i) + (e*j) == f:
      print(i, j)
      break