# 비슷한 단어
import sys; input=sys.stdin.readline

cnt = int(input()) # 단어의 개수
word = list(input().rstrip()) # 첫 번째 단어
res = 0


for _ in range(cnt-1):
  word_copy = word[:]
  tmp = list(input().rstrip()) # 비교할 단어
  cnt = 0
  
  for i in tmp:
    if i in word_copy:
      word_copy.remove(i)
    else:
      cnt += 1
  if cnt <= 1 and len(word_copy) <= 1:
    res += 1
else:
  print(res)
  
