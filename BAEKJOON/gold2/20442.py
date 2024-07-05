# ㅋㅋ루ㅋㅋ
import sys;input=sys.stdin.readline

s = input().rstrip()

start, end = 0, 0
N = len(s)
res = 0
while end < N:
    if s[end] == 'R':
        end += 1
    else:
        if s[start] 