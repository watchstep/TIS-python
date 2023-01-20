# 별 찍기 - 19

N = int(input())

def star_1(n):
  return '*'*(4*n-3)

def star_2(n):
  return '*'+ ' '*(4*n-5) + '*'

# 재귀 사용
def star(n):
  if n == 1:
    res = "*"
  else:
    before_star = []
    for s in star(n-1):
      before_star.append('* ' + s + ' *')
    res = [star_1(n), star_2(n)]
    res.extend(before_star+[star_2(n), star_1(n)])
  return res

for s in star(N):
  print(s)

# 다른 풀이
N = int(input())

def add_before_star(one_line):
  return '* ' + one_line + ' *'

def star(n):
  if n == 1:
    res = '*'
  else:
    star_1 = '*'*(4*n-3)
    star_2 = '*'+ ' '*(4*n-5) + '*'
    res = [star_1, star_2] + list(map(add_before_star, star(n-1))) + [star_2, star_1]
  return res

print('\n'.join(star(N)))