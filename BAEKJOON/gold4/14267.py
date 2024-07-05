# 회사 문화 1
import sys;input=sys.stdin.readline

n, m = map(int, input().split())
boss = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for _ in range(m):
    i, w = map(int, input().split()) # 직원 index 1부터 시작
    dp[i] += w # 일단 직원이 받은 칭찬 

for i in range(2, n+1):
    dp[i] += dp[boss[i-1]]  # 상사의 칭찬 스티커 추가

print(*dp[1:])

