# 투에-모스 문자열
import sys;input=sys.stdin.readline

k = int(input())

def find_kth(x):
    if  x == 0:
        return 0
    elif x == 1:
        return 1
    elif x % 2 == 0:
        return find_kth(x // 2) # t_2n = t_n
    else:
        return 1 - find_kth(x // 2) # t_{2n+1} = 1 - t_n
    
print(find_kth(k - 1))

###################################
import sys;input=sys.stdin.readline

k = int(input())

k -= 1
res = 0
while(k):
    res += k%2
    k //= 2

print(res % 2)