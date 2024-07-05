# 가르침
import sys;input=sys.stdin.readline

N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]

N -= 4 # a n t i c (4개는 꼭 읽을 줄 알아야함)
alpha = ["a", "n", "t", "i", "c"]
filtered = []
# anta tica
for w in words:
    w = w[4:-4]
    w = "".join(a for a in set(w) if a not in alpha)
    filtered.append(w)
    