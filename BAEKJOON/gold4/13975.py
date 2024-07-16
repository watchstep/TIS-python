# 파일 합치기 3
import sys;input=sys.stdin.readline

T = int(input())
pages = [list(map(int, input().split())) for _ in range(T)]

K = int(input())
files = [int(input()) for _ in range(K)]

# 여러 장으로 나누어 쓰기
# min_heap= 