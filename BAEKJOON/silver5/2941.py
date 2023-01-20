import sys

# /n 개행문자 없이 input
word = sys.stdin.readline().strip()

permutations = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


def count(word):
  total = len(word)
  sub = 0
  
  for p in permutations:
    sub += word.count(p) 
    
  total -= sub
  
  print(total)

count(word)

