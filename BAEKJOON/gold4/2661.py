# 좋은수열
import sys;input=sys.stdin.readline
N = int(input())

def is_bad(n):
    mid = len(n) // 2
    for i in range(1, mid + 1):
        if n[-i:] == n[-2*i:-i]:
            return True
    return False

def back(n):
    if is_bad(n):
        return
    if len(n) == N:
        print(n)
        exit()
    for i in '123':
        back(n + i)
        
back('')