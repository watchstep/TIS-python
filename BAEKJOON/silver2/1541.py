# 잃어버린 괄호
import sys
input = sys.stdin.readline

# '-' 를 기준으로 먼저 나누어 최솟값 만들기
exp = input().rstrip().split('-')

res = sum([int(j) for j in exp[0].split('+')])

for i in exp[1:]:
  res -= sum([int(j) for j in i.split('+')])

print(res)