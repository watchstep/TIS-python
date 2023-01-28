# 늑대와 올바른 단어
import sys
from collections import Counter
input = sys.stdin.readline

word = input().rstrip()

# ex) Counter({'w': 2, 'o': 2, 'l': 2, 'f': 2})
cnt_dict = Counter(word)
cnt = cnt_dict.values()

# [2, 2, 2, 2] -> {2} 모두 개수가 같으면, 유니크한 값이 1개
if len(set(cnt)) == 1:
  # w 개수
  cnt_w = list(cnt)[0]
  check = 'w'*cnt_w + 'o'*cnt_w + 'l'*cnt_w + 'f'*cnt_w
  if word == check:
    # 올바른 단어 하나 있는 경우 ex) wwoollff
    print(1)
  else:
    # ex) wwoollffwolf w개수 3개인데 올바른 단어 2개 (wwoollff), (wolf)로 이루어진 경우
    for _ in range(cnt_w):
      cnt_w -= 1
      # wwoollff가 있으면 공백으로 대체
      check = 'w'*cnt_w + 'o'*cnt_w + 'l'*cnt_w + 'f'*cnt_w
      if check in word:
        word = word.replace(check, '')
    else:
      if len(word) == 0:
        print(1)
      else:
        print(0)
else:
  # 개수가 같지 않은 경우  
  print(0)