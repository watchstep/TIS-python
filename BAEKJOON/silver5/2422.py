# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
import sys
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())
no_mix = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
icecreams = list(range(1, N+1))

# n_C_3
cnt = N*(N-1)*(N-2) // 6


  

