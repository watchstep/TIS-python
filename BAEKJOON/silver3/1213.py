# 팰린드롬 만들기
from collections import Counter
# 문자열을 넘기면, 각 문자가 문자열에서 몇 번씩 나타나는지 알려줌
import sys; input = sys.stdin.readline

hansoo = input().rstrip()
alphabet_cnt = Counter(hansoo)

cnt = 0
res = ''
center = ''
for k, v in list(alphabet_cnt.items()):
  


  
  