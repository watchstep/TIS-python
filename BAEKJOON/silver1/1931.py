# 회의실 배정
import sys
input = sys.stdin.readline

N = int(input())

session = []
for _ in range(N):
  session.append(list(map(int, input().split())))

session.sort(key=lambda x: (x[1], x[0]))
session_start = [s[0] for s in session]
session_end = [s[1] for s in session]
cnt = 1
idx = 0
end = session_end[idx]

for s in session_start[idx+1:]:
  if s >= end:
    end = session_end[idx+1]
    cnt += 1
    pass
  idx += 1
else:
  print(cnt)
  
  
# 다른 풀이
import sys
input = sys.stdin.readline

N = int(input())

session = []
for _ in range(N):
  session.append(list(map(int, input().split())))

session.sort(key=lambda x: (x[1], x[0]))

end = 0
cnt = 0

for s, e in session:
  if s >= end:
    cnt += 1
    end = e
    
print(cnt)