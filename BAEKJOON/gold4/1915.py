# 가장 큰 정사각형
import sys;input=sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
