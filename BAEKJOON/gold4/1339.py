# 단어 수학
import sys;input = sys.stdin.readline
from collections import Counter

N = int(input())
words = [input().rstrip() for _ in range(N)]
word_dict = Counter()

