# 동전 게임
import sys;input=sys.stdin.readline

T = int(input())
for _ in range(T):
    arr = [input().split() for _ in range(3)]

# 한 행 모든 동전
# 한 열의 모든 동전
# 한 대각선 상의 모든 동전
arr = [input().split() for _ in range(3)]
def flip_coin(i, j):
    arr[i][j] = 'F' if arr[i][j] == 'T' else 'T'



def flip_coin_row(row):
     