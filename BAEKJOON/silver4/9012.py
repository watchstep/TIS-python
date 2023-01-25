# 괄호
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  ps = input().rstrip()
  # '()'가 없을 때까지 '()'를 없애기
  while '()' in ps:
    ps = ps.replace('()', '')
  # 만약 '()' 를 다 없앴는데, 길이가 1 이상이면 (괄호가 남아있으면) 'N0' 출력
  else:
    if len(ps) == 0:
      print('YES')
    else:
      print('NO')

# 다른 풀이 1
import sys
input = sys.stdin.readline

T = int(input())
res = ''

for _ in range(T):
  ps = input().rstrip()
  cnt = 0
  for p in ps:
    # '(' 이면 cnt += 1, ')' 이면 cnt -= 1
    cnt += 1 if p == '(' else -1
    # cnt < 0이면, 완전히 괄호가 닫힌 게 아니므로 'NO' 출력 (닫는 괄호가 더 많음)
    if cnt < 0:
      res += 'NO\n'
      break
  else:
    # cnt == 0이면, 올바르게 괄호가 닫혔으므로, 'YES' 출력
    # cnt > 0이면, 여는 괄호가 더 많음 'NO' 출력
    res += 'YES\n' if cnt == 0 else 'NO\n'
    
print(res)

# 다른 풀이 2
import sys
input = sys.stdin.readline

T = int(input())
res = ''

for _ in range(T):
  ps = input().rstrip()
  stack = []
  for p in ps:
    if p == '(':
      stack.append(p)
    elif p == ')':
      # stack이 비어있지 않은 경우
      if stack:
        # '()' 완성
        stack.pop()
      else:
        # '('이 없고, ')'만 있어서 '()' 완성 X
        res += 'NO\n'
        break
  else:
    # break문 실행 안되고, stack이 비어있는 경우 '()' 모두 완성했을 때
    if not stack:
      res += 'YES\n'
    else:
      res += 'NO\n'
      
print(res)
      
