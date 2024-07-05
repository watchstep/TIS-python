# 배열 돌리기 1
import sys;input=sys.stdin.readline

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr_tr = list(map(list, list(zip(*arr)))) # transpose
new_arr = [[0]*M for _ in range(N)] # col M row N

from collections import deque
t = deque(arr)
t
t.rotate(1)
t
arr
indices = []
indices += [()]