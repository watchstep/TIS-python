# LCS 2
import sys;input=sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

n, m = len(s1), len(s2)
dp = [[0]*(m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# backtracking
lcs = ''
i, j = n, m
while (i > 0) and (j > 0):
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        i -= 1
        j -= 1
        lcs += s1[i]
        
print(dp[-1][-1])
if lcs:
    print(lcs[::-1])
    
#######################################
import sys;input=sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

n, m = len(s1), len(s2)
dp = [[""]*(m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
        else:
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

if len(dp[n][m]):
    print(len(dp[n][m]))
    print(dp[n][m])
else:
    print(0)