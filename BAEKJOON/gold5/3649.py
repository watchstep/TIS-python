# 로봇 프로젝트
import sys;input=sys.stdin.readline

def bin_search():
    n_lens.sort()
    start, end = 0, n - 1
    while start < end:
        if n_lens[start] + n_lens[end] == x:
            print(f"yes {n_lens[start]} {n_lens[end]}")
            break
        elif n_lens[start] + n_lens[end] < x:
            start += 1
        else:
            end -= 1
    else:
        print("danger")
        
while True:
    try:
        x = int(input())*10000000 # 구멍의 너비 (센티미터)
        n = int(input()) # 레고 조각 수
        n_lens = [int(input()) for _ in range(n)] # 레고 조각 길이 (나노미터)
        bin_search()
    except:
        break
    