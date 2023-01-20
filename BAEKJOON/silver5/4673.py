def generator(n):
  digit_lst = [int(i) for i in list(str(n))]
  res = n + sum(digit_lst)
  
  return res

lst = list(range(1, 10001))
generator_set = set()

for i in lst:
  res = generator(i)
  generator_set.add(generator(i))

for i in lst:
  if i not in generator_set:
    print(i)

