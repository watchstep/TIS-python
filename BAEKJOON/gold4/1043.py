# 거짓말
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
know_list = set(input().split()[1:])
graph = []

for i in range(m):
  graph.append(set(input().split()[1:]))

for _ in range(m):
  for n in graph:
    if n & know_list:
      know_list = know_list.union(n)
      
cnt = 0
for n in graph:
  if n & know_list:
    continue
  cnt += 1
  
print(cnt)
    