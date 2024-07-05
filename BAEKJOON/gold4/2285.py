# 우체국
import sys;input=sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

min_val = 1e9
res = -1
for i in range(N):
    tmp = 0
    for j in range(N):
        if i != j:
            tmp += arr[j][1]*abs(arr[i][0] - arr[j][0])
    if min_val > tmp:
        min_val = tmp
        res = arr[i][0]
        
print(res)


# 1 -> 3명 0, 5명 1, 3명 2 = 5*1 + 3*2 = 11
# 2 -> 3명 1, 5명 0, 3명 1 = 3*1 + 3*1 = 6
# 3 -> 3명 2, 5명 1, 3명 0 = 3*2 + 5*1 = 11
# 절대 안되는구나... N^2 NlogN 
# half_num_people 절반인 이유
# 우체국으로 양쪽
# 절반을 포함한 시점에서 최고의 값이다....

