# 팰린드롬 만들기
from collections import Counter
import sys; input = sys.stdin.readline

hansoo = input().rstrip()
alphabet_cnt = Counter(hansoo)

odd_cnt = 0
center = ''
res = ''

for k, v in sorted(alphabet_cnt.items()): # 사전순
  # 알파벳 개수가 홀수인 경우 (ex A가 3개 있는 경우)
  if v % 2 == 1:
    odd_cnt += 1
    center = k # 알파벳 개수가 홀수인 경우, 중간에 들어가야함
    if odd_cnt >= 2: # 홀수 개수인 알파벳이 2개 이상이면 펠린드롬 X
      print("I'm Sorry Hansoo")
      exit()
  res += (k*(v//2))

print(res+center+res[::-1])
