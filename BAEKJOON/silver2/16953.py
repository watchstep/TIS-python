# A → B
import sys
input = sys.stdin.readline

A, B = map(int, input().split())

cnt = 1

# A -> B (bottom-up) 가 아니라 B -> A (top-down)를 만들기
while A != B:
  cnt += 1
  check = B
  # 끝에서 1 빼기
  if B % 10 == 1:
    B //= 10
  # 2로 나누기
  elif B % 2 == 0:
    B //= 2
    
  # 위의 두 방법으로 B에서 A를 못 만들 경우
  if check == B:
    print(-1)
    break
else:
  print(cnt)