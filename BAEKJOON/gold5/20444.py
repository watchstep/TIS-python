# 색종이와 가위
import sys;input=sys.stdin.readline

n, k = map(int, input().split())
# n번의 가위질로 k개의 색종이 조각을 만들 수 있다면 
# 1 2개 2 4개 3 6개  4 8개 9개 
# 이게 어떻게 이분탐색인데
def is_possible():
    