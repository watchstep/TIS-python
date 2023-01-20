# 단어 정렬
N = int(input())

words_dict = dict()

for _ in range(N):
  word = input()
  words_dict.update({word : len(word)})

# dictionary key 정렬 (sorted 하면 list로 변경됨)
words_list = sorted(words_dict.items(), key=lambda x : x[0])
words_list
# value 정렬 (sorted 하면 list로 변경됨)
words_list = sorted(words_list, key=lambda x : x[1])
words_list

for k, v in words_list:
  print(k)


# 다른 풀이
N = int(input())

words = list()

for _ in range(N):
  words.append(input())

# 중복 제거 & 사전 순으로 정렬
words = sorted(list(set(words)))

# 길이가 짧은 순으로 정렬
words.sort(key=lambda x : len(x))

for word in words:
  print(word)
