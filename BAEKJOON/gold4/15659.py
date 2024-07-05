# 연산자 끼워넣기 (3)
import sys;input=sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split())) # +, -, *, //
# 우선순위 이용
