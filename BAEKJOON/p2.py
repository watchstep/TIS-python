def solution(n):
    dp = [0]*(n + 1)
    dp[1] = 2

    if n == 1:
        return dp[1]

    for i in range(2, n + 1):
        dp[i] = i*(i + 1)
        for j in range(1, i):
            dp[i] = min(dp[i], dp[j]*i)
    return dp

import heapq
from sys import stdin

####################### 지훈님 코드
def get_nth_cont_mul(n):
    visit = set([2])
    cont_muls = [2]
    queue = [(6, 2, 3)]
    while True:
        p, s, e = heapq.heappop(queue)
        if p not in visit:
            visit.add(p)
            cont_muls.append(p)
            if len(cont_muls) == n:
                return cont_muls[n - 1]
        # Same window with the next sequence.
        heapq.heappush(queue, (p * (e + 1) // s, s + 1, e + 1))
        # Larger window with the same start.
        heapq.heappush(queue, (p * (e + 1), s, e + 1))


N = int(stdin.readline())
print(get_nth_cont_mul(N))