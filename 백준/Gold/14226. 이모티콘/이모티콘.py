import sys;input=sys.stdin.readline
from collections import deque

S = int(input())
q = deque([])

q = deque([(1, 0, 0)]) # screen, clip, cnt
visited = set([(1, 0)]) # (screen, clip)

def bfs():
	while q:
		screen, clip, cnt = q.popleft()
		if screen == S:
			return cnt 
		
		if (screen, screen) not in visited:
			q.append((screen, screen, cnt + 1)) # 복사
			visited.add((screen, screen))

		if clip > 0 and (screen + clip, clip) not in visited:
			q.append((screen + clip, clip, cnt + 1)) # 붙여넣기
			visited.add((screen + clip, clip))

		if screen > 1 and (screen - 1, clip) not in visited:
			q.append((screen - 1, clip, cnt + 1)) # 삭제
			visited.add((screen - 1, clip))


print(bfs())