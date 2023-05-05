# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
import sys; input = sys.stdin.readline

n, m = map(int, input().split())
nomix = []
for _ in range(m):
  a, b = map(int, input().split())
  nomix.append((a, b))
  
cnt = n*(n-1)*(n-2) // 6

nomix

