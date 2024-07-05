# 팰린드롬?
import sys;input=sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [[0 for _ in range(N)] for _ in range(N)]
# 1개일 때는 무조건 팰린드롬
for i in range(N):
    dp[i][i] = 1

# 2개일 때는 두 숫자가 같으면 팰린드롬
for i in range(N - 1):
    if arr[i] == arr[i + 1]:
        dp[i][i + 1] = 1
    else:
        dp[i][i + 1] = 0
        
# 3개 이상일 때는 양 끝이 같고, 그 사이가 팰린드롬이면 팰린드롬
for num_len in range(2, N):
    for start in range(N - num_len):
        end = start + num_len
        if (arr[start] == arr[end]) and (dp[start + 1][end - 1] == 1):
            dp[start][end] = 1
      
M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])
