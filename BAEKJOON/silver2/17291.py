# 새끼 치기
import sys;input=sys.stdin.readline
N = int(input())

dp = [0]*21
dp[0], dp[1] = 1, 1

for i in range(2, N+1):
    dp[i] = dp[i - 1]*2
    # 홀수년, 짝수년에 태어난 벌레 모두 짝수년도에 사망
    # 1년생 4년에 사망, 2년생 6년에 사망
    if i % 2 == 0:
        dp[i] -= dp[i - 4] + dp[i - 5]
    
print(dp[N])
