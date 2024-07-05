# 보석 상자
import sys; input=sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(M)]

# lo <= hi, lo < hi, lo + 1 < hi
# 