# LCS 3
import sys;input=sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
s3 = input().rstrip()

def get_lcs3(a, b, c):
    n, m, l = len(a), len(b), len(c)
    dp = [[[0]*(l+1) for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l+1):
                if (a[i - 1] == b[j - 1]) and (b[j - 1] == c[k - 1]):
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1 
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1]) # max(위쪽, 왼쪽)
                
    return dp[-1][-1][-1]

print(get_lcs3(s1, s2, s3))