# 파일 탐색기
import sys;input=sys.stdin.readline

N = int(input())
before = [input().rstrip() for _ in range(N)]

def natural_sort(a, b):
    for i in range(min(len(a), len(b))):
        # 둘 다 숫자
        if a[i].isalnum() and b[i].isalnum():
            a_num = ''
            b_num = ''
            