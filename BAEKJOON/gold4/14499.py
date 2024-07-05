# 주사위 굴리기
import sys;input=sys.stdin.readline

N, M, X, Y, K = map(int, input().split())
mmap = [list(map(int, input().split())) for _ in range(N)]
cmd = list(map(int, input().split()))