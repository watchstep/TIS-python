# ㄷㄷㄷㅈ
import sys;input=sys.stdin.readline

N = int(input())
degrees = [0]*(N+1)
edges = []
for _ in range(N-1):
    a, b = map(int, input().split())
    degrees[a] += 1
    degrees[b] += 1
    edges.append((a, b))
    
def is_g(a): # degree_C_3
    if degrees[a] >= 3:
        return degrees[a] * (degrees[a] - 1) * (degrees[a] - 2) / 6
    return 0

def is_d(a, b):
    return (degrees[a] - 1) * (degrees[b] - 1)

g = 0
d = 0

for a in range(1, N+1):
    g += is_g(a)

for a, b in edges:
    d += is_d(a, b)
    
if d > 3*g:
    print('D')
elif d < 3*g:
    print('G')
else:
    print('DUDUDUNGA')