# 비밀번호 발음하기
vowels = 'aeiou'

# 모음 하나 이상 반드시 포함
def check_vowels(password):
  for i in password:
    if i in vowels:
     return True
  return False

# 모음/자음 3개 연속 안됨
def check_triple(password):
  if len(password) > 2:
    for i in range(len(password)-2):
      if password[i] in vowels and password[i+1] in vowels and password[i+2] in vowels:
        return False
      elif password[i] not in vowels and password[i+1] not in vowels and password[i+2] not in vowels:
        return False
  return True


# 같은 글자 연속 2번 안됨 ('ee', 'oo'만 허용)
def check_twice(password):
  if len(password) > 1:
    for i in range(len(password)-1):
     if password[i] == password[i+1] and password[i] not in 'eo':
        return False
  return True

while True:
  password = input()
  if password == 'end':
    break
  if check_vowels(password) & check_triple(password) & check_twice(password):
    print(f'<{password}> is acceptable.')
  else:
    print(f'<{password}> is not acceptable.')

