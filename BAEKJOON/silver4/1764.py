# 듣보잡
import sys;input=sys.stdin.readline
from collections import Counter

N, M = map(int, input().split())
n_arr = [input().rstrip() for _ in range(N)]
m_arr = [input().rstrip() for _ in range(M)]

nm_arr = list(set(n_arr)) + list(set(m_arr))
counter = Counter(nm_arr)
res = []
for c in counter:
    if counter[c] == 2:
        res.append(c)
res.sort()
print(len(res))
print(*res, sep='\n')

# 다른 풀이
import sys;input=sys.stdin.readline
from collections import Counter

N, M = map(int, input().split())
n_arr = [input().rstrip() for _ in range(N)]
m_arr = [input().rstrip() for _ in range(M)]

res = list(set(n_arr) & set(m_arr))
res.sort()
print(len(res))
print(*res, sep='\n')