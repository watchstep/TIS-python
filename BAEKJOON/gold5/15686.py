# 치킨 배달
import sys;input=sys.stdin.readline

N, M = map(int, input().split())
home = []
chichken = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            home.append((i, j))
        elif row[j] == 2:
            chichken.append((i, j))

def get_dist(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

# dfs 참고
visited = [False]*len(chichken)
min_dist = 1e9

def dfs(idx=0, cnt=0):
    global min_dist
    if cnt == M:
        tmp = 0
        for h in home:
            h_dist = 1e9
            for c in range(len(chichken)):
                if visited[c]:
                    ttmp = get_dist(h[0], h[1], chichken[c][0], chichken[c][1])
                    # 최소 치킨 거리
                    h_dist = min(ttmp, h_dist)
            # 치킨 거리 총합
            tmp += h_dist
        min_dist = min(tmp, min_dist)
        
        return

    for c in range(idx, len(chichken)):
        if not visited[c]:
            visited[c] = True
            dfs(c + 1, cnt + 1)
            visited[c] = False            
            
dfs()
print(min_dist)