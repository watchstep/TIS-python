# 나무꾼 이다솜
import sys;input=sys.stdin.readline

N, C, W = map(int, input().split())
tree = [int(input()) for _ in range(N)]
max_profit = 0

def get_profit(a):
    profit = 0
    for t in tree:
        q, r = t // a, t % a
        if r:
            cost = q*C
        else: # 나누어 떨어지면
            cost = (q-1)*C
    
        tmp = q*a*W - cost
        if tmp < 0:
            continue # 예제 3 고려 해당 나무 사용했을 때 이익이 없다면
        
        profit += tmp
    
    return profit

for i in range(1, max(tree) + 1):
    tmp = get_profit(i)
    max_profit = max(max_profit, tmp)

print(max_profit)

