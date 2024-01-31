# N결수
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
n_nect = ''.join(list(map(str, range(1, n+1))))
n_nect = int(n_nect)
# 붙이는 것은 어떻게 해야할까..?
# 123456789
# 붙이고 난 다음에 나눠야하는 수보다 크면
# 바로 나누 다음에
# 몫에 붙이고 붙임...
print(n_nect%k)
