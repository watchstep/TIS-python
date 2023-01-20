# 그룹단어 체커
N = int(input())

lst = []

for _ in range(N):
  lst.append(input())
  
# 연속된 중복 문자 제거
def remove_duplicate(word):
  new = ''
  prev = None
  
  for i in word:
    if prev != i:
      new += i
      prev = i
      
  return new

res = 0

for word in lst:
  # 연속된 중복 문자 제거
  not_duplicate_word = remove_duplicate(word)
  # 고유 문자만
  unique_word = set(word)
  if sorted(not_duplicate_word) == sorted(set(word)):
    res += 1
    
print(res)

'''
다른 풀이
'''
N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)
