# 원 이동하기 2
import sys;input=sys.stdin.readline
import math

N = int(input())
circles = [list(map(int, input().split())) for _ in range(N)]
A, B = map(int, input().split())

def get_dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

