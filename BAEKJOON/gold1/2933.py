# 미네랄
import sys;input=sys.stdin.readline
from collections import deque

R, C =  map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
N = int(input())
height = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs()