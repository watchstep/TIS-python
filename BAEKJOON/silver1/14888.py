def dfs(res, i, add, sub, mul, div):
    global N
    if i == N:
        res_li.append(res)
    else:
        if add:
            dfs(res + nums[i], i+1, add-1, sub, mul, div)            
        if sub:
            dfs(res - nums[i], i+1, add, sub-1, mul, div)
        if mul:
            dfs(res * nums[i], i+1, add, sub, mul-1, div)
        if div:
            dfs(int(res / nums[i]), i+1, add, sub, mul, div-1)          
    
N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
res_li = []

dfs(nums[0], 1, add, sub, mul, div)
print(max(res_li))
print(min(res_li))