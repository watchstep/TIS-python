# 연산자 끼워넣기
###################### 순열
import sys;input=sys.stdin.readline 
sys.setrecursionlimit(10**5) # Python으로 하면 시간초과 PyPy로 하니까 되긴됨

N = int(input())
nums = list(map(int, input().split()))
operators_cnt = list(map(int, input().split()))  # + - x //
operators = []
for i in range(4):
    if operators_cnt[i] == 0: # 0*"+" = ''
        continue
    if i == 0:
        operators.extend(operators_cnt[i]*['+'])
    elif i == 1:
        operators.extend(operators_cnt[i]*['-'])
    elif i == 2:
        operators.extend(operators_cnt[i]*['x'])
    else:
        operators.extend(operators_cnt[i]*['//'])
        
def cal(ops):
    res = nums[0]
    for n, op in zip(nums[1:], ops):
        if op == '+':
            res += n 
        elif op == '-':
            res -= n 
        elif op == 'x':
            res *= n 
        elif op == '//':
            if res < 0:
                res = - res
                res //= n
                res = - res
            elif res > 0:
                res //= n
    return res

tmp = []
visited = [False]*(N - 1)
vals = []
def dfs():
    if len(tmp) == N - 1:
        vals.append(cal(tmp))
        return
    for i in range(N - 1):
        if not visited[i]:
            visited[i] = True
            tmp.append(operators[i])
            dfs()
            tmp.pop()
            visited[i] = False
        
dfs()

print(max(vals))
print(min(vals))


########################### 백트래킹
import sys;input=sys.stdin.readline 

N = int(input())
nums = list(map(int, input().split()))
operators_cnt = list(map(int, input().split()))  # + - x //
