# 별 찍기 - 10
import sys
input = sys.stdin.readline

N = int(input())

def star_recursion(n):
  if n == 1:
    pattern = ['***', '* *', '***'] 
    return pattern
  before = star_recursion(n//3)
  p1 = list(map(lambda x:x*3, before))
  p2 = list(map(lambda x: x+' '*n+x, before))
  pattern = p1 + p2 + p1
  return pattern

print('\n'.join(star_recursion(N//3)))

